#!/usr/bin/env python3
"""翻訳処理部分だけ切り出したもの。"""

import argparse
import logging
import os
import pathlib
import re
import sys
import typing

import openai
import tiktoken
import tqdm

from translatedoc import utils

logger = logging.getLogger(__name__)


def main():
    """メイン関数。"""
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

    parser = argparse.ArgumentParser(description="Translate text file.")
    parser.add_argument(
        "--output-dir",
        "-o",
        default=pathlib.Path("."),
        type=pathlib.Path,
        help="output directory (default: .)",
    )
    parser.add_argument(
        "--force", "-f", action="store_true", help="overwrite existing files"
    )
    parser.add_argument(
        "--language",
        "-l",
        default="Japanese",
        help="target language name (default: Japanese)",
    )
    parser.add_argument(
        "--api-key",
        "-k",
        default=os.environ.get("OPENAI_API_KEY"),
        help="OpenAI API key (default: OPENAI_API_KEY environment variable)",
    )
    parser.add_argument(
        "--api-base",
        "-b",
        default=os.environ.get("OPENAI_API_BASE"),
        help="OpenAI API base URL (default: OPENAI_API_BASE environment variable)",
    )
    parser.add_argument(
        "--model",
        "-m",
        default=os.environ.get("TRANSLATEDOC_MODEL", "gpt-3.5-turbo-1106"),
        help="model (default: gpt-3.5-turbo-1106)",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="verbose mode")
    parser.add_argument(
        "input_files", nargs="+", type=pathlib.Path, help="input text files"
    )
    args = parser.parse_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    openai_client = openai.OpenAI(api_key=args.api_key, base_url=args.api_base)

    exit_code = 0
    for input_path in tqdm.tqdm(args.input_files, desc="Input files/URLs"):
        try:
            # テキストファイルの読み込み
            text = input_path.read_text(encoding="utf-8")

            # 翻訳
            output_path = (
                args.output_dir / input_path.with_suffix(f".{args.language}.txt").name
            )
            if utils.check_overwrite(output_path, args.force):
                output_path.parent.mkdir(parents=True, exist_ok=True)
                with output_path.open("w") as file:
                    tqdm.tqdm.write(f"Translating {input_path}...")
                    chunks = partition(text, args.model)
                    for chunk in tqdm.tqdm(chunks, desc="Chunks"):
                        output_chunk = translate(
                            str(chunk), args.model, args.language, openai_client
                        )
                        file.write(output_chunk.strip() + "\n\n")
                        file.flush()
                tqdm.tqdm.write(f"{output_path} written.")
        except Exception as e:
            logger.error(f"{e} ({input_path})")
            exit_code = 1

    sys.exit(exit_code)


def partition(text: str, model: str, max_chunk_size: int | None = None) -> list[str]:
    """翻訳用に分割する。"""
    # 最大チャンクサイズの決定: 翻訳前提ならコンテキスト長の1/3くらいでいい気もするが安全を見て1/4
    if max_chunk_size is None:
        system_prompt_tokens = 100  # システムプロンプトの大体のトークン数
        max_tokens = max_tokens_from_model_name(model)
        logger.debug(f"{max_tokens=}")
        max_chunk_size = (max_tokens - system_prompt_tokens) // 4
        logger.debug(f"{max_chunk_size=}")

    encoding = tiktoken.encoding_for_model(model)

    # 基本は改行2つ以上で区切る
    base_parts = re.split(r"\n\n+", text)

    # max_chunk_sizeを超えないトークン数ずつチャンクにしていく
    chunks: list[tuple[str, int]] = []
    for base_part in base_parts:
        base_part_tokens = len(encoding.encode(base_part))
        if base_part_tokens <= max_chunk_size:
            # max_chunk_size以下ならそのまま追加
            chunks.append((base_part, base_part_tokens))
        else:
            # base_partを更に分割
            chunk = ""
            chunk_tokens = 0
            for part, part_tokens in zip(
                *_sub_partition(base_part, max_chunk_size, encoding), strict=True
            ):
                # 今回のpartを追加するとチャンクサイズを超える場合、いったんそこで区切る
                if chunk_tokens + part_tokens > max_chunk_size:
                    assert chunk != "" and chunk_tokens > 0
                    chunks.append((chunk, chunk_tokens))
                    chunk, chunk_tokens = "", 0
                # チャンクに追加する
                chunk += part
                chunk_tokens += part_tokens
            if chunk != "":
                chunks.append((chunk, chunk_tokens))

    return _merge_chunks(chunks, max_chunk_size, encoding)


def _merge_chunks(
    chunks: list[tuple[str, int]], max_chunk_size: int, encoding: tiktoken.Encoding
) -> list[str]:
    """複数のチャンクを結合してもmax_chunk_size以下なところは結合していく。"""
    chunk_sep = "\n\n"
    chunk_sep_tokens = len(encoding.encode(chunk_sep))

    combined_chunks: list[str] = []
    combined_chunk = ""
    combined_chunk_tokens = 0
    for chunk, chunk_tokens in chunks:
        # 今回のpartを追加するとチャンクサイズを超える場合、いったんそこで区切る
        if combined_chunk_tokens + chunk_sep_tokens + chunk_tokens > max_chunk_size:
            assert combined_chunk != "" and combined_chunk_tokens > 0
            combined_chunks.append(combined_chunk)
            combined_chunk, combined_chunk_tokens = "", 0
        # combined_chunkに追加する (セパレーター付き)
        if combined_chunk != "":
            combined_chunk += chunk_sep
            combined_chunk_tokens += chunk_sep_tokens
        combined_chunk += chunk
        combined_chunk_tokens += chunk_tokens

    # 最後のチャンク
    if combined_chunk != "":
        combined_chunks.append(combined_chunk)

    return combined_chunks


def _sub_partition(
    text: str, max_chunk_size: int, encoding: tiktoken.Encoding, separator="\n"
) -> tuple[list[str], list[int]]:
    """textをmax_chunk_sizeを超えないサイズに分割していく。"""
    parts: list[str] = []
    parts_tokens: list[int] = []

    # 基本は改行2つ以上で区切る
    # 改行区切りである程度分かれるならそれ単位
    # それでもだめならスペース区切り
    # 最終手段として区切りを考えず
    next_separator = {"\n": " ", " ": ""}[separator]
    separator_token_count = len(encoding.encode(separator))

    base_parts = list(_split_with_separator(text, separator))

    # separatorで分割して1つずつ見ていく
    for part in base_parts:
        assert part != ""
        encoded = encoding.encode(part)
        part_tokens = len(encoded)
        # max_chunk_size以下ならOK
        if part_tokens + separator_token_count <= max_chunk_size:
            parts.append(part)
            parts_tokens.append(part_tokens)
            continue
        # 超えてたら更に分割
        if next_separator != "":
            sub_parts, sub_part_tokens = _sub_partition(
                part, max_chunk_size, encoding, next_separator
            )
            parts.extend(sub_parts)
            parts_tokens.extend(sub_part_tokens)
            continue
        # 最終手段、トークン単位でぶつ切り
        for offset in range(0, len(encoded), max_chunk_size):
            tokens = encoded[offset : offset + max_chunk_size]
            parts.append(encoding.decode(tokens))
            parts_tokens.append(len(tokens))

    return parts, parts_tokens


def _split_with_separator(
    text: str, separator: str
) -> typing.Generator[str, None, None]:
    """separatorで分割し、separatorを含めて返す。"""
    index = 0
    while True:
        next_index = text.find(separator, index)
        if next_index == -1:
            break
        next_index += len(separator)
        yield text[index:next_index]
        index = next_index
    yield text[index:]


def translate(
    chunk: str, model: str, language: str, openai_client: openai.OpenAI
) -> str:
    """翻訳。"""
    response = openai_client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": f"Translate the input into {language}."
                " Do not output anything other than the translation result."
                " Do not translate names of people, mathematical formulas,"
                " source code, URLs, etc.",
            },
            {"role": "user", "content": chunk},
        ],
        temperature=0.0,
    )
    if len(response.choices) != 1 or response.choices[0].message.content is None:
        return f"*** Unexpected response: {response.model_dump()=} ***"
    return response.choices[0].message.content


def max_tokens_from_model_name(model: str) -> int:
    """OpenAIのモデル名から最大トークン数を返す。

    Args:
        model: モデル名。

    Returns:
        最大トークン数。

    """
    max_tokens = MODEL_MAX_TOKENS.get(model)
    if max_tokens is None:
        logger.warning(f"Unknown model: {model}")
        if "gpt-4" in model:
            return 8192
        return 4096
    return max_tokens


# https://platform.openai.com/docs/models/gpt-3-5-turbo
# https://platform.openai.com/docs/models/gpt-4-and-gpt-4-turbo
MODEL_MAX_TOKENS = {
    "gpt-3.5-turbo": 4096,
    "gpt-3.5-turbo-0613": 4096,
    "gpt-3.5-turbo-1106": 16385,
    "gpt-3.5-turbo-0125": 16385,
    "gpt-3.5-turbo-16k": 16385,
    "gpt-3.5-turbo-16k-0613": 16385,
    "gpt-3.5-turbo-instruct": 4096,
    "gpt-4": 8192,
    "gpt-4-0613": 8192,
    "gpt-4-32k": 32768,
    "gpt-4-32k-0613": 32768,
    "gpt-4-turbo-preview": 128000,
    "gpt-4-1106-preview": 128000,
    "gpt-4-0125-preview": 128000,
    "gpt-4-vision-preview": 128000,
}

if __name__ == "__main__":
    main()
