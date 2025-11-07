from preproc_pkg import create_spell_pipeline

if __name__ == "__main__":
    txt = "اصلاح متون فارسی با ابزار Parsivar کاربردی است. کتاب کوآنتومی خوندم."

    pipe = create_spell_pipeline()
    print("Original :", txt)
    print("Corrected (Parsivar):", pipe(txt))

    # sp_pipe = create_spell_pipeline(
    #     use_parsivar=False,
    #     use_transformer=True,
    #     model_name="your-org/persian-spell-t5"
    # )
    # print("Corrected (Transformer only):", sp_pipe(txt))
