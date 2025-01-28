"""
    Author: Alireza Parvaresh
    Email: parvvaresh@gmail.com
    LinkedIn: https://www.linkedin.com/in/parvvaresh/
"""

import re

def remove_diacritics(text: str) -> str:
    """
    This function removes Arabic diacritics (e.g., Tashdid, Fatha, Damma, etc.) and Tatwil/Kashida from the input text.

    Parameters:
        text (str): The input text from which diacritics need to be removed.

    Returns:
        str: The text after removing all diacritics.
    """
    # Defining a regular expression pattern to match Arabic diacritics and Tatwil/Kashida
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
    
    # Removing the matched diacritics from the text using re.sub
    text = re.sub(arabic_diacritics, '', text)

    # Returning the cleaned text
    return text
