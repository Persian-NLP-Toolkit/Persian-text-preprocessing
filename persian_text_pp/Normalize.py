"""
Author: Alireza Parvaresh
Email: parvvaresh@gmail.com
LinkedIn: https://www.linkedin.com/in/parvvaresh/
"""

import re
from dadmatools.normalizer import Normalizer


def normalize_arabic(text):
    """
    Normalizes Arabic characters to their Persian equivalents.

    This includes:
    - Replacing Arabic Alef variants with Persian Alef.
    - Replacing Arabic Yeh with Persian Yeh.
    - Replacing Arabic Waw with Hamza to Persian Waw.
    - Replacing Arabic Yeh with Hamza to Persian Yeh.
    - Replacing Arabic Teh Marbuta to Persian Heh.
    - Replacing Arabic Kaf to Persian Kaf.

    Parameters:
        text (str): The input text to be normalized.

    Returns:
        str: The text with Arabic characters normalized to Persian.
    """
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ي", "ی", text)
    text = re.sub("ؤ", "و", text)
    text = re.sub("ئ", "ی", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("ك", "ک", text)
    return text


def normalize_persian(text: str, unify_chars: bool = True, refine_punc_spacing: bool = True, remove_html: bool = False, replace_email_with: str = "<EMAIL>", replace_number_with: str = None, replace_url_with: str = "", replace_mobile_number_with: str = None, replace_emoji_with: str = None, replace_home_number_with: str = None) -> str:
    """
    Normalizes Persian text using DadmaTools' Normalizer and additional cleaning steps.

    This includes:
    - Applying Arabic normalization.
    - Refining punctuation spacing.
    - Removing HTML tags if specified.
    - Replacing specific patterns like emails, numbers, URLs, etc.
    - Removing extra spaces and zero-width non-joiners.

    Parameters:
        text (str): The input text to be normalized.
        unify_chars (bool): Whether to unify characters.
        refine_punc_spacing (bool): Whether to refine punctuation spacing.
        remove_html (bool): Whether to remove HTML tags.
        replace_email_with (str): Replacement for email addresses.
        replace_number_with (str): Replacement for numbers.
        replace_url_with (str): Replacement for URLs.
        replace_mobile_number_with (str): Replacement for mobile numbers.
        replace_emoji_with (str): Replacement for emojis.
        replace_home_number_with (str): Replacement for home numbers.

    Returns:
        str: The normalized Persian text.
    """
    text = normalize_arabic(text)

    normalizer = Normalizer(
        unify_chars=unify_chars,
        refine_punc_spacing=refine_punc_spacing,
        remove_html=remove_html,
        replace_email_with=replace_email_with,
        replace_number_with=replace_number_with,
        replace_url_with=replace_url_with,
        replace_mobile_number_with=replace_mobile_number_with,
        replace_emoji_with=replace_emoji_with,
        replace_home_number_with=replace_home_number_with
    )

    text = normalizer.normalize(text)

    # Remove non-Persian characters and clean up spacing
    text = re.sub("[^ابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی]", " ", text)
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('\u200c', '').strip()

    return text
