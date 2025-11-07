from preproc_pkg import create_stem_pipeline

if __name__ == "__main__":
    txt = "آن‌ها کتاب‌هایشان را آوردند و می‌خواندند."
    print("Original:", txt)
    print("Stem (present, default):", create_stem_pipeline()(txt))
    print("Stem (past):", create_stem_pipeline(prefer_past=True)(txt))
