from persian_text_pp.FarsiLanguageRecognition import is_farsi
from persian_text_pp.Normalize import normalize_text
from persian_text_pp.RemoveDiacritics import remove_diacritics
from persian_text_pp.RemovePunctuations import remove_punctuations
from persian_text_pp.RemoveRepeatingChar import remove_repeating_chars
from persian_text_pp.RemoveStopWords import remove_stopwords
from persian_text_pp.Tokenize import tokenize
from persian_text_pp.Lemmatizer import lemmatize



class PreprocessPipeline:
    """
    A class that encapsulates the preprocessing pipeline for Persian text.

    This class provides methods to preprocess Persian text through various steps,
    including normalization, tokenization, stopword removal, and lemmatization.
    """

    def __init__(self):
        """
        Initializes the PreprocessPipeline with customizable options.

        """
        pass

    def preprocess_pipeline(self,
                            text):
        """
        Preprocesses Persian text through all standard steps and returns tokens.

        Steps applied (in order):
        1. Detect Farsi language
        2. Normalize text
        3. Remove diacritics
        4. Remove punctuation
        5. Remove repeating characters
        6. Tokenize
        7. Remove stopwords
        8. Lemmatize


        Returns:
            list: The preprocessed tokens.
        """
        # Step 1: Detect if the text is Persian
        if not is_farsi(text):
            raise ValueError("The input text is not in Persian.")

        # Step 2: Normalize the text
        text = normalize_text(text)

        # Step 3: Remove diacritics
        text = remove_diacritics(text)

        # Step 4: Remove punctuation
        text = remove_punctuations(text)

        # Step 5: Remove repeating characters
        text = remove_repeating_chars(text)

        # Step 6: Tokenize the text
        tokens = tokenize(text)

        # Step 7: Remove stopwords (operates on tokens)
        tokens = remove_stopwords(tokens)

        # Step 8: Lemmatize (operates on tokens)
        tokens = lemmatize(tokens)

        return tokens







# pp = PreprocessPipeline()

# text = """در ادامه تلاطم در بازارهای مالی دنیا و نگرانی از وقوع رکود اقتصادی، قیمت جهانی طلا در صبح روز سه‌شنبه با رسیدن به مرز ۳۵۰۰ دلار رکورد تازه‌ای در تاریخ ثبت کرد.


#         ▫️ وضعیت دلار

#         در پی انتقادهای دونالد ترامپ از بانک مرکزی ایالات متحده و افزایش نگرانی‌ها دربارهٔ استقلال این نهاد، دلار آمریکا روز سه‌شنبه در برابر ین به پایین‌ترین سطح جدیدی رسید و در برابر یورو و فرانک سوئیس نیز در نزدیکی کف‌های چندساله نوسان کرد.

#         تحلیل‌گران، تعرفه‌های تجاری آمریکا و احتمال وقوع جنگ تجاری جهانی را عامل شکنندگی بیشتر دلار دانسته‌اند. همچنین، اعلام تعویق مذاکرات تجاری میان تایلند و واشینگتن به افت بیشتر ارزش دلار انجامید.
#         """


# for e in (pp.preprocess_pipeline(text)):
#     print(e)

# ادامه
# تلاطم
# بازار
# مالی
# دنیا
# نگران
# وقوع
# رکود
# اقتصاد
# قیمت
# جهانی
# طلا
# صبح
# سه‌شنبه
# مرز
# دلار
# رکورد
# تازه
# تاریخ
# ثبت
# وضعیت
# دلار
# انتقاد
# دونالد
# ترامپ
# بانک
# مرکزی
# ایالات‌متحده
# افزایش
# نگرانی‌ها
# استقلال
# نهاد
# دلار
# امریکا
# سه‌شنبه
# ین
# پاین‌ترین
# سطح
# جدید
# یورو
# فرانک
# سویس
# نزدیک
# کف
# چندساله
# نوسان
# تحلیل
# گران
# تعرفه
# تجار
# امریکا
# احتمال
# وقوع
# جنگ
# تجار
# جهانی
# عامل
# شکندگی
# دلار
# دانست#دان
# تعویق
# مذاکرات
# تجار
# تایلند
# واشینگتن
# افت
# ارزش
# دلار
# انجامید