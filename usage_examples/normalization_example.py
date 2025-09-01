from preproc_pkg.normalizer_pkg import (
    normalize,
    HazmNormalizer,
    ParsivarNormalizer,
)
from preproc_pkg.normalizer_pkg.cleaners import html, url, nonbmp, collapse_spaces
from preproc_pkg.normalizer_pkg.pinglish import convert as pinglish_convert

RAW = """
<h1>سلاممم!!!</h1> miam khoneh 😊
visit https://foo.com 12345
"""

print("=== pipeline ===")
print(normalize(RAW))
print()

print("=== using only Hazm (custom switches) ===")
hz_only = HazmNormalizer(
    correct_spacing=True,
    persian_numbers=True,
    decrease_repeated_chars=True,
)
print(hz_only(RAW))
print()

print("=== individual cleaners ===")
stage1 = html.process(RAW)
stage2 = url.process(stage1)
stage3 = nonbmp.process(stage2)
stage4 = collapse_spaces.process(stage3)
print(stage4)
print()

print("=== Parsivar only, forced Pinglish conversion ===")
pv_only = ParsivarNormalizer(pinglish_conversion_needed=True)
print(pv_only("salam chetori? man khoneh miram."))
