"""
Author: Alireza Parvaresh
Email: parvvaresh@gmail.com
LinkedIn: https://www.linkedin.com/in/parvvaresh/
"""

from langdetect import detect, DetectorFactory, LangDetectException

# Setting seed for consistent language detection results
DetectorFactory.seed = 0

def is_farsi(text: str) -> bool:
    """
    Determines whether a given text is written in Farsi (Persian).

    Parameters:
        text (str): The input text to be checked.

    Returns:
        bool: True if the text is Farsi, otherwise False.
    """
    try:
        # Detect the language of the text and check if it is Farsi (language code 'fa')
        return detect(text) == 'fa'
    except LangDetectException:
        # If language detection fails, return False
        return False
