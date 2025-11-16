from preproc_pkg import create_normalizer_pipeline


def main():
    demo = (
        "به @ali ایمیل بزن: test+foo@mail.example.com — شماره‌اش 09123456789 و #سلام! https://foo.bar"
        "\n\n\n"
        "خط دوم   با   فاصله‌ها"
    )

    print("=== pipeline (Parsivar + Hazm، با کلینرهای اجتماعی) ===")
    pipe = create_normalizer_pipeline(
        enable_quotes_dashes=True,
        enable_url=True,
        enable_email=True,
        enable_mention=True,
        enable_hashtag=True,
        enable_phone=True,
        enable_nonbmp=True,
        enable_pinglish=True,
        enable_parsivar=True,
        enable_hazm=True,
        enable_metrics=True,
    )
    text, rep = pipe(demo, return_report=True)
    print(text)
    print("metrics (ms):", rep["timings_ms"])
    print()

    print("=== Parsivar ONLY ===")
    pipe_pv_only = create_normalizer_pipeline(
        enable_quotes_dashes=True,
        enable_url=True,
        enable_email=True,
        enable_mention=True,
        enable_hashtag=True,
        enable_phone=True,
        enable_nonbmp=True,
        enable_pinglish=True,
        enable_parsivar=True,
        enable_hazm=False,
        parsivar_cfg={"token_punctuation_augmentation": False},
    )
    print(pipe_pv_only(demo))
    print()

    print("=== Hazm ONLY ===")
    pipe_hz_only = create_normalizer_pipeline(
        enable_quotes_dashes=True,
        enable_url=True,
        enable_email=True,
        enable_mention=True,
        enable_hashtag=True,
        enable_phone=True,
        enable_nonbmp=True,
        enable_pinglish=True,
        enable_parsivar=False,
        enable_hazm=True,
    )
    print(pipe_hz_only(demo))
    print()

    demo_para = "خط اول\n\n\n\nخط دوم    با    فاصله‌ها"

    print("=== default collapse (بدون حفظ پاراگراف) ===")
    print(
        create_normalizer_pipeline(enable_parsivar=False, enable_hazm=False)(demo_para)
    )

    print("=== collapse_keep_newlines=True (حفظ پاراگراف‌ها) ===")
    print(
        create_normalizer_pipeline(
            enable_parsivar=False, enable_hazm=False, collapse_keep_newlines=True
        )(demo_para)
    )


if __name__ == "__main__":
    main()
