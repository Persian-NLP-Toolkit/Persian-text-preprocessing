# Persian Text Preprocessing Toolkit

این مخزن شامل ابزارهایی برای پیش‌پردازش متن‌های فارسی است. با استفاده از این ابزارها می‌توانید متون فارسی را برای تحلیل‌های بعدی (مانند تحلیل احساسات، طبقه‌بندی متون، خوشه‌بندی و غیره) آماده کنید.

---

##  ساختار پوشه‌ها و فایل‌ها

```
persian_text_pp/
├── FarsiLanguageRecognition.py      # تشخیص زبان فارسی
├── Normalize.py                     # نرمال‌سازی اولیه متن
├── RemoveDiacritics.py              # حذف علائم اعراب
├── RemovePunctuations.py            # حذف علامت‌های نگارشی
├── RemoveRepeatingChar.py           # حذف کاراکترهای تکراری
├── Informal2Formal.py               # تبدیل غیررسمی به رسمی
├── Tokenize.py                      # توکنایز (شکستن متن به کلمات)
├── RemoveStopWords.py               # حذف کلمات توقف
├── Lemmatizer.py                   # لماتیزه کردن (ریشه‌یابی کلمات)
└── PreprocessPipeline.py            # پایپ‌لاین پیش‌پردازش

get_stopwords/
├── get_stopwords.py                  # بارگذاری لیست کلمات توقف
└── persian_stopwords/                # فایل‌های خام لیست توقف
    ├── chars.txt
    ├── nonverbal.txt
    ├── persian.txt
    ├── short.txt
    └── verbal.txt
```

### توضیح فایل‌ها

- **FarsiLanguageRecognition.py**  
  ورودی: `str` — متن ورودی  
  خروجی: `bool` — آیا متن فارسی است یا خیر

- **Normalize.py**  
  تابع اصلی: `normalize_persian(text: str, unify_chars: bool = True, refine_punc_spacing: bool = True, remove_html: bool = False, replace_email_with: str = "<EMAIL>", replace_number_with: Optional[str] = None, replace_url_with: str = "", replace_mobile_number_with: Optional[str] = None, replace_emoji_with: Optional[str] = None, replace_home_number_with: Optional[str] = None) -> str`  
  عملیات: یکسان‌سازی کاراکترها، تنظیم فاصله‌های علائم، حذف HTML، جایگزینی آدرس‌ها/اعداد/URLها و غیره

- **RemoveDiacritics.py**  
  حذف کلیه علائم اعراب (فتحه، کسره، ضمه و …)

- **RemovePunctuations.py**  
  حذف کلیه نشانه‌های نگارشی مانند `.,!?؛…`

- **RemoveRepeatingChar.py**  
  تبدیل توالی‌های تکراری یک کاراکتر به یک نمونه (مثلاً `عاااالی` → `عالی`)

- **Informal2Formal.py**  
  اصلاح لغات غیررسمی به معادل رسمیشان

- **Tokenize.py**  
  شکستن متن به توکن‌های لغوی با توجه به قواعد فارسی

- **RemoveStopWords.py**  
  حذف کلمات توقف از لیست توکن‌ها

- **Lemmatizer.py**  
  تبدیل هر توکن به ریشه واژه با استفاده از کتابخانه Hazm

- **PreprocessPipeline.py**  
  تعریف تابع `preprocess_pipeline(...)` برای اجرای تمام مراحل به ترتیب و بازگرداندن لیستی از توکن‌های نهایی.

---

##  پایپ‌لاین پیش‌پردازش

تابع اصلی در `PreprocessPipeline.py` به شکل زیر تعریف شده است:

```python
from persian_text_pp.FarsiLanguageRecognition import detect_farsi
from persian_text_pp.Normalize import normalize_persian
from persian_text_pp.RemoveDiacritics import remove_diacritics
from persian_text_pp.RemovePunctuations import remove_punctuations
from persian_text_pp.RemoveRepeatingChar import remove_repeating_char
from persian_text_pp.Informal2Formal import informal_to_formal
from persian_text_pp.Tokenize import tokenize
from persian_text_pp.RemoveStopWords import remove_stopwords
from persian_text_pp.Lemmatizer import lemmatize


def preprocess_pipeline(
    text: str,
    unify_chars: bool = True,
    refine_punc_spacing: bool = True,
    remove_html: bool = False,
    replace_email_with: str = "<EMAIL>",
    replace_number_with: str = None,
    replace_url_with: str = "",
    replace_mobile_number_with: str = None,
    replace_emoji_with: str = None,
    replace_home_number_with: str = None,
) -> list:
    """
    Full preprocessing pipeline for Persian text returning tokens.

    Args:
        text (str): Input Persian text.
        unify_chars (bool): Whether to unify similar characters.
        refine_punc_spacing (bool): Whether to adjust spacing around punctuation.
        remove_html (bool): Whether to strip HTML tags.
        replace_email_with (str): Replacement text for email addresses.
        replace_number_with (Optional[str]): Replacement for numeric tokens.
        replace_url_with (str): Replacement text for URLs.
        replace_mobile_number_with (Optional[str]): Replacement for mobile numbers.
        replace_emoji_with (Optional[str]): Replacement for emojis.
        replace_home_number_with (Optional[str]): Replacement for landline numbers.

    Returns:
        List[str]: List of processed tokens.
    """
    # 1. Verify input is Persian
    if not detect_farsi(text):
        raise ValueError("Input text is not Persian.")

    # 2. Normalize text with provided options
    text = normalize_persian(
        text,
        unify_chars=unify_chars,
        refine_punc_spacing=refine_punc_spacing,
        remove_html=remove_html,
        replace_email_with=replace_email_with,
        replace_number_with=replace_number_with,
        replace_url_with=replace_url_with,
        replace_mobile_number_with=replace_mobile_number_with,
        replace_emoji_with=replace_emoji_with,
        replace_home_number_with=replace_home_number_with,
    )

    # 3. Remove diacritics
    text = remove_diacritics(text)

    # 4. Remove punctuation characters
    text = remove_punctuations(text)

    # 5. Normalize repeated characters
    text = remove_repeating_char(text)

    # 6. Convert informal text to formal register
    text = informal_to_formal(text)

    # 7. Split text into tokens
    tokens = tokenize(text)

    # 8. Remove stopwords from token list
    tokens = remove_stopwords(tokens)

    # 9. Lemmatize tokens
    tokens = lemmatize(tokens)

    return tokens
```

---

##  نصب پیش‌نیازها

```bash
pip install -r requirements.txt
```

---

##  مثال استفاده

```python
from persian_text_pp.PreprocessPipeline import preprocess_pipeline

text = "این یک متن آزمایشی است! شماره تماس: 0912-345-6789"
# همه مراحل را با تنظیمات پیش‌فرض اجرا می‌کند
tokens = preprocess_pipeline(text)
print(tokens)
# ['این', 'یک', 'متن', 'آزمایشی', 'است', 'شماره', 'تماس', '09123456789']
```

---

*با خوشحالی پذیرای پیشنهادات و Pull Requestهای شما هستیم!*

