from preproc_pkg import create_spell_pipeline

if __name__ == "__main__":
    txt = "اصلاح متون فارسی با ابزار Parsivar کاربدی است. کتاب کوآنتومی خوندم."
    pipe = create_spell_pipeline()  # Parsivar by default
    print("Original :", txt)
    print("Corrected:", pipe(txt))
