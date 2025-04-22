"""
Author: Alireza Parvaresh
Email: parvvaresh@gmail.com
LinkedIn: https://www.linkedin.com/in/parvvaresh/
"""

import re
from hazm import word_tokenize

def informal2formal(text: str) -> str:
    """
    Converts informal Persian text to its formal equivalent.

    Parameters:
        text (str): The input informal Persian text.

    Returns:
        str: The formalized Persian text.
    """
    # Tokenize the input text using Hazm
    tokens = word_tokenize(text)

    # Define a dictionary containing informal Persian phrases (keys)
    # and their formal equivalents (values).
    conversion_dict = {
        r"\bمیخوام\b": "می‌خواهم",
        r"\bنمیخوام\b": "نمی‌خواهم",
        r"\bمیریم\b": "می‌رویم",
        r"\bبخوام\b": "بخواهم",
        r"\bمیگم\b": "می‌گویم",
        r"\bمیگه\b": "می‌گوید",
        r"\bمیگن\b": "می‌گویند",
        r"\bبریم\b": "برویم",
        r"\bبرمیگردیم\b": "بازمی‌گردیم",
        r"\bنمیدونم\b": "نمی‌دانم",
        r"\bنمیتونم\b": "نمی‌توانم",
        r"\bنمیشه\b": "نمی‌شود",
        r"\bبزار\b": "بگذار",
        r"\bبده\b": "بدهد",
        r"\bمیدم\b": "می‌دهم",
        r"\bمیدن\b": "می‌دهند",
        r"\bدارم\b": "دارم",
        r"\bندارم\b": "ندارم",
        r"\bچطوری\b": "چگونه",
        r"\bمیبینم\b": "می‌بینم",
        r"\bاینو\b": "این را",
        r"\bاونجا\b": "آنجا",
        r"\bاینکه\b": "این‌که",
        r"\bاون\b": "آن",
        r"\bدلم میخواد\b": "دوست دارم",
        r"\bچیکار کنم\b": "چه‌کار کنم",
        r"\bکی\b": "چه‌کسی",
        r"\bکجا\b": "در کجا",
        r"\bحالا\b": "اکنون",
        r"\bالان\b": "در حال حاضر",
        r"\bآره\b": "بله",
        r"\bنه\b": "خیر",
        r"\bباشه\b": "باشد",
        r"\bمیخواستم\b": "می‌خواستم",
        r"\bبخواستم\b": "بخواهم",
        r"\bخوبه\b": "خوب است",
        r"\bهمینه\b": "همین است",
        r"\bچرا\b": "به چه دلیل",
        r"\bمیشه\b": "می‌شود",
        r"\bمیکنم\b": "می‌کنم",
        r"\bکردن\b": "انجام دادن",
        r"\bمیکنه\b": "می‌کند",
    }

    # Replace informal tokens with their formal equivalents
    formal_tokens = [re.sub(pattern, formal, token) for token in tokens for pattern, formal in conversion_dict.items()]

    # Join the tokens back into a single string
    formal_text = " ".join(formal_tokens)

    return formal_text
