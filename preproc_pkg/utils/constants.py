# preproc_pkg/utils/constants.py
import re

# Shared punctuation set for Persian-aware detokenization.
PUNCT = {"،", ".", "!", "؟", "؛", ":", "…", "»", "«", "(", ")", "[", "]", ","}

# Shared split regex used by Hazm/Parsivar to encode past|present.
SPLIT_RE = re.compile(r"[#&|/]+")
