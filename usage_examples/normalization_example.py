from preproc_pkg import create_normalizer_pipeline

print("=== pipeline (factory, with social cleaners on) ===")
pipe = create_normalizer_pipeline(
    enable_quotes_dashes=True,
    enable_url=True,
    enable_email=True,
    enable_mention=True,
    enable_hashtag=True,
    enable_phone=True,
    enable_nonbmp=True,
    enable_pinglish=True,
)
demo = "به @ali ایمیل بزن: test+foo@mail.example.com — شماره‌اش 09123456789 و #سلام! https://foo.bar"
print(pipe(demo))
print()

print("=== pipeline (Parsivar ONLY) ===")
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
)
print(pipe_pv_only(demo))
print()

print("=== pipeline (Hazm ONLY) ===")
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
    parsivar_cfg={"token_punctuation_augmentation": False},
)
print(pipe_hz_only(demo))
print()
