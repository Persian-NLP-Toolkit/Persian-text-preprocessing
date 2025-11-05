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
