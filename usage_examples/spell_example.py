from preproc_pkg import create_spell_pipeline

if __name__ == "__main__":
    txt = "اسلاح متون قارسي با ابزار Parsivar كاربردي است. كتاب كوآنتومي خوندم."
    pipe = create_spell_pipeline()
    print("Original :", txt)
    print("Corrected:", pipe(txt))
