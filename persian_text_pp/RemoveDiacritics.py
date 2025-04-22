"""
Author: Alireza Parvaresh
Email: parvvaresh@gmail.com
LinkedIn: https://www.linkedin.com/in/parvvaresh/
"""

import re

def remove_diacritics(text: str) -> str:
    """
    Removes Arabic diacritics (e.g., Tashdid, Fatha, Damma, etc.) and Tatwil/Kashida from the input text.

    Parameters:
        text (str): The input text from which diacritics need to be removed.

    Returns:
        str: The text after removing all diacritics.
    """
    arabic_diacritics = re.compile("""
        ّ    | # Tashdid
        َ    | # Fatha
        ً    | # Tanwin Fath
        ُ    | # Damma
        ٌ    | # Tanwin Damm
        ِ    | # Kasra
        ٍ    | # Tanwin Kasr
        ْ    | # Sukun
        ـ     # Tatwil/Kashida
    """, re.VERBOSE)

    return re.sub(arabic_diacritics, '', text)
