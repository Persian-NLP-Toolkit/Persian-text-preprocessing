from preproc_pkg import create_stopword_pipeline

if __name__ == "__main__":
    text = "این یک متن نمونه است که در آن برخی از کلمات بی‌اهمیت وجود دارد."
    pipe = create_stopword_pipeline()
    print("Original     :", text)
    print("No stopwords :", pipe(text))
