set -euo pipefail

preproc-cli --version

preproc-cli normalize --text "سلام    دنیا  —  اینجا  تست  است."
preproc-cli spell --text "اصلاح متون فارسی با ابزار Parsivar کاربدی است. کتاب کوآنتومی خوندم."
preproc-cli formal --text "میخوام برم"  # needs extra: [formalizer]
preproc-cli lemma --text "آن‌ها کتاب‌هایشان را آوردند و می‌خواندند."
preproc-cli stem --text "آن‌ها کتاب‌هایشان را آوردند و می‌خواندند."
preproc-cli stopword --text "این یک متن نمونه است که در آن برخی از کلمات بی‌اهمیت وجود دارد."