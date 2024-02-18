"""translatedocをライブラリとして使うとき用。"""

from .step1 import extract_text
from .step2 import partition, translate

__all__ = ["extract_text", "partition", "translate"]
