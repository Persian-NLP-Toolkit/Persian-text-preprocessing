"""
    Author: Alireza Parvaresh
    Email: parvvaresh@gmail.com
    LinkedIn: https://www.linkedin.com/in/parvvaresh/
"""
import re



def normalize_persian(text):
    """
    This function normalizes Persian text by replacing Arabic characters with their Persian equivalents,
    removing non-Persian characters, and cleaning up spacing issues.

    Parameters:
        text (str): The input text to be normalized.

    Returns:
        str: The normalized Persian text.
    """
    # Normalize Arabic Alef variants to Persian Alef
    text = re.sub("[إأآا]", "ا", text)

    # Normalize Arabic Yeh to Persian Yeh
    text = re.sub("ي", "ی", text)

    # Normalize Arabic Waw with Hamza to Persian Waw
    text = re.sub("ؤ", "و", text)

    # Normalize Arabic Yeh with Hamza to Persian Yeh
    text = re.sub("ئ", "ی", text)

    # Normalize Arabic Teh Marbuta to Persian Heh
    text = re.sub("ة", "ه", text)

    # Normalize Arabic Kaf to Persian Kaf
    text = re.sub("ك", "ک", text)

    # Remove any non-Persian characters (retain only Persian letters and spaces)
    text = re.sub("[^ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی]", " ", text)

    # Replace multiple spaces (including tabs and newlines) with a single space
    text = re.sub(r'\s+', ' ', text)

    # Remove zero-width non-joiner (نیم‌فاصله)
    text = text.replace('\u200c', '')

    # Strip leading and trailing spaces
    text = text.strip()

    return text
