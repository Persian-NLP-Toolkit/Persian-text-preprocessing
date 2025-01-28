"""
Author: Alireza Parvaresh
Email: parvvaresh@gmail.com
LinkedIn: https://www.linkedin.com/in/parvvaresh/
"""

import re

def informal2formal(text : str) -> str:
    # Define a dictionary containing informal Persian phrases (keys)
    # and their formal equivalents (values).
    conversion_dict = {
        r"\bمیخوام\b": "می‌خواهم",  # Informal "میخوام" -> Formal "می‌خواهم"
        r"\bنمیخوام\b": "نمی‌خواهم",  # Informal "نمیخوام" -> Formal "نمی‌خواهم"
        r"\bمیریم\b": "می‌رویم",      # Informal "میریم" -> Formal "می‌رویم"
        r"\bبخوام\b": "بخواهم",      # Informal "بخوام" -> Formal "بخواهم"
        r"\bمیگم\b": "می‌گویم",      # Informal "میگم" -> Formal "می‌گویم"
        r"\bمیگه\b": "می‌گوید",      # Informal "میگه" -> Formal "می‌گوید"
        r"\bمیگن\b": "می‌گویند",    # Informal "میگن" -> Formal "می‌گویند"
        r"\bبریم\b": "برویم",       # Informal "بریم" -> Formal "برویم"
        r"\bبرمیگردیم\b": "بازمی‌گردیم", # Informal "برمیگردیم" -> Formal "بازمی‌گردیم"
        r"\bنمیدونم\b": "نمی‌دانم",  # Informal "نمیدونم" -> Formal "نمی‌دانم"
        r"\bنمیتونم\b": "نمی‌توانم",  # Informal "نمیتونم" -> Formal "نمی‌توانم"
        r"\bنمیشه\b": "نمی‌شود",    # Informal "نمیشه" -> Formal "نمی‌شود"
        r"\bبزار\b": "بگذار",       # Informal "بزار" -> Formal "بگذار"
        r"\bبده\b": "بدهد",         # Informal "بده" -> Formal "بدهد"
        r"\bمیدم\b": "می‌دهم",      # Informal "میدم" -> Formal "می‌دهم"
        r"\bمیدن\b": "می‌دهند",    # Informal "میدن" -> Formal "می‌دهند"
        r"\bدارم\b": "دارم",       # Informal "دارم" -> Formal "دارم"
        r"\bندارم\b": "ندارم",     # Informal "ندارم" -> Formal "ندارم"
        r"\bچطوری\b": "چگونه",     # Informal "چطوری" -> Formal "چگونه"
        r"\bمیبینم\b": "می‌بینم",  # Informal "میبینم" -> Formal "می‌بینم"
        r"\bاینو\b": "این را",     # Informal "اینو" -> Formal "این را"
        r"\bاونجا\b": "آنجا",      # Informal "اونجا" -> Formal "آنجا"
        r"\bاینکه\b": "این‌که",    # Informal "اینکه" -> Formal "این‌که"
        r"\bاون\b": "آن",           # Informal "اون" -> Formal "آن"
        r"\bدلم میخواد\b": "دوست دارم",  # Informal "دلم میخواد" -> Formal "دوست دارم"
        r"\bچیکار کنم\b": "چه‌کار کنم",  # Informal "چیکار کنم" -> Formal "چه‌کار کنم"
        r"\bکی\b": "چه‌کسی",       # Informal "کی" -> Formal "چه‌کسی"
        r"\bکجا\b": "در کجا",     # Informal "کجا" -> Formal "در کجا"
        r"\bحالا\b": "اکنون",     # Informal "حالا" -> Formal "اکنون"
        r"\bالان\b": "در حال حاضر",  # Informal "الان" -> Formal "در حال حاضر"
        r"\bآره\b": "بله",         # Informal "آره" -> Formal "بله"
        r"\bنه\b": "خیر",          # Informal "نه" -> Formal "خیر"
        r"\bباشه\b": "باشد",       # Informal "باشه" -> Formal "باشد"
        r"\bمیخواستم\b": "می‌خواستم",  # Informal "میخواستم" -> Formal "می‌خواستم"
        r"\bبخواستم\b": "بخواهم",  # Informal "بخواستم" -> Formal "بخواهم"
        r"\bخوبه\b": "خوب است",    # Informal "خوبه" -> Formal "خوب است"
        r"\bهمینه\b": "همین است",  # Informal "همینه" -> Formal "همین است"
        r"\bچرا\b": "به چه دلیل",   # Informal "چرا" -> Formal "به چه دلیل"
        r"\bمیشه\b": "می‌شود",     # Informal "میشه" -> Formal "می‌شود"
        r"\bمیکنم\b": "می‌کنم",    # Informal "میکنم" -> Formal "می‌کنم"
        r"\bکردن\b": "انجام دادن", # Informal "کردن" -> Formal "انجام دادن"
        r"\bمیکنه\b": "می‌کند",    # Informal "میکنه" -> Formal "می‌کند"
        r"\bدست میارم\b": "به دست می‌آورم", # Informal "دست میارم" -> Formal "به دست می‌آورم"
        r"\bبرگردیم\b": "بازگردیم", # Informal "برگردیم" -> Formal "بازگردیم"
        r"\bمنم\b": "من هم",        # Informal "منم" -> Formal "من هم"
        r"\bتوئه\b": "تو است",      # Informal "توئه" -> Formal "تو است"
        r"\bخودم\b": "به خودم",     # Informal "خودم" -> Formal "به خودم"
        r"\bخودش\b": "به خودش",    # Informal "خودش" -> Formal "به خودش"
        r"\bخودمون\b": "به خودمان", # Informal "خودمون" -> Formal "به خودمان"
        r"\bخودتون\b": "به خودتان", # Informal "خودتون" -> Formal "به خودتان"
        r"\bخودشون\b": "به خودشان", # Informal "خودشون" -> Formal "به خودشان"
        r"\bاگه\b": "اگر",         # Informal "اگه" -> Formal "اگر"
    }

    # Iterate over each pattern in the conversion dictionary.
    # Replace all occurrences of the informal pattern in the input sentence
    # with its corresponding formal equivalent.
    for pattern, formal in conversion_dict.items():
        text = re.sub(pattern, formal, text)

    # Return the modified (formalized) sentence.
    return text
