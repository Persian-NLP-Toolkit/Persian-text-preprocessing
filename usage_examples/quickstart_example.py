from preproc_pkg import (
    create_normalizer_pipeline,
    create_spell_pipeline,
    create_formal_pipeline,
    create_stopword_pipeline,
    create_lemma_pipeline,
    create_stem_pipeline,
)


def main():
    raw = "میخوام    آدرس www.example.com رو بفرستم؛ شماره‌اش 09123456789 ــ اوکیه؟"
    print(">>> RAW:")
    print(raw)
    print()

    # 1) Normalizer
    norm = create_normalizer_pipeline(enable_metrics=True)
    normalized, report = norm(raw, return_report=True)
    print(">>> NORMALIZED:")
    print(normalized)
    print("\n--- metrics (ms):", report.get("timings_ms", {}))
    print()

    # 2) Spell (Parsivar-based)
    spell = create_spell_pipeline()
    spelled = spell(
        "اصلاح متون فارسی با ابزار Parsivar کاربدی است. کتاب کوآنتومی خوندم."
    )
    print(">>> SPELL (Parsivar):")
    print(spelled)
    print()

    # 3) Formal (T5)  -> needs install extra: [formalizer]
    try:
        formal = create_formal_pipeline()  
        print(">>> FORMAL:")
        print(formal("اسمم محمده، میخوایم بریم بیرون؛ دوستم منتظرم وایستاده."))
    except Exception as e:
        print(">>> FORMAL skipped (install extra: `preproc-pkg[formalizer]`):", e)
    print()

    # 4) Stopword
    sw = create_stopword_pipeline()
    print(">>> STOPWORD:")
    print(sw("این یک متن نمونه است که در آن برخی از کلمات بی‌اهمیت وجود دارد."))
    print()

    # 5) Lemma
    lemma_present = create_lemma_pipeline(prefer_past=False)
    lemma_past = create_lemma_pipeline(prefer_past=True)
    txt = "آن‌ها کتاب‌هایشان را آوردند و می‌خواندند."
    print(">>> LEMMA (present):", lemma_present(txt))
    print(">>> LEMMA (past):   ", lemma_past(txt))
    print()

    # 6) Stem
    stem_present = create_stem_pipeline(prefer_past=False)
    stem_past = create_stem_pipeline(prefer_past=True)
    print(">>> STEM  (present):", stem_present(txt))
    print(">>> STEM  (past):   ", stem_past(txt))


if __name__ == "__main__":
    main()
