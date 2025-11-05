from preproc_pkg import create_lemma_pipeline

if __name__ == "__main__":
    txt = "آن‌ها کتاب‌هایشان را آوردند و می‌خواندند."
    print("Original:", txt)
    print("Lemma (present stem, default):", create_lemma_pipeline()(txt))
    print("Lemma (past stem):", create_lemma_pipeline(prefer_past=True)(txt))
