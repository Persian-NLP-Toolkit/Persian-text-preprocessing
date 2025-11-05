from preproc_pkg import create_stem_pipeline

if __name__ == "__main__":
    txt = "آن‌ها کتاب‌هایشان را آوردند و می‌خواندند."
    print("Original:", txt)
    print("Stem (present, default):", create_stem_pipeline()(txt))
    print("Stem (past):", create_stem_pipeline(prefer_past=True)(txt))


# from preproc_pkg import create_stem_pipeline

# text = "آن‌ها کتاب‌هایشان را آوردند و می‌خواندند."
# pipeline = create_stem_pipeline()  # use_hazm=True, use_parsivar=True by default
# print("Original text:", text)
# print("Stemmed text:", pipeline(text))

# # Compare with Hazm-only and Parsivar-only
# print("Hazm stemmed:", create_stem_pipeline(use_hazm=True, use_parsivar=False)(text))
# print(
#     "Parsivar stemmed:", create_stem_pipeline(use_hazm=False, use_parsivar=True)(text)
# )
