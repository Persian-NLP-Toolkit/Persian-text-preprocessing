from preproc_pkg import create_stopword_pipeline

if __name__ == "__main__":
    text = "این یک متن نمونه است که در آن برخی از کلمات بی‌اهمیت وجود دارد."
    pipe = create_stopword_pipeline()
    print("Original:", text)
    print("No stopwords:", pipe(text))


# from preproc_pkg import create_stopword_pipeline
# from hazm import stopwords_list

# text = "این یک متن نمونه است که در آن برخی از کلمات بی‌اهمیت وجود دارد."
# pipeline = create_stopword_pipeline()
# print("Original text:", text)
# print("Without stopwords:", pipeline(text))

# # Demonstrating that Hazm's stopwords_list contains words like "این", "از", etc.
# stops = set(stopwords_list())
# sample_tokens = ["این", "نمونه", "از", "کلمات"]
# print("Stopword tokens in sample:", [t for t in sample_tokens if t in stops])
