# Version
preproc-cli --version

# Normalize
preproc-cli normalize --text "سلام    دنیا  —  اینجا  تست  است."

# Spell (Parsivar)
preproc-cli spell --text "اصلاح متون فارسی با ابزار Parsivar کاربدی است. کتاب کوآنتومی خوندم."

# Formal (needs extra: formalizer)
preproc-cli formal --text "میخوام برم"

# Lemma
preproc-cli lemma --text "آن‌ها کتاب‌هایشان را آوردند و می‌خواندند."

# Stem
preproc-cli stem --text "آن‌ها کتاب‌هایشان را آوردند و می‌خواندند."

# Stopword
preproc-cli stopword --text "این یک متن نمونه است که در آن برخی از کلمات بی‌اهمیت وجود دارد."
