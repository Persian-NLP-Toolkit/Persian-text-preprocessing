"""
Author: Alireza Parvaresh
Email: parvvaresh@gmail.com
LinkedIn: https://www.linkedin.com/in/parvvaresh/
"""

import re
import hazm

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

def remove_html_tags(text):
    """
    Removes HTML tags from the input text.

    Args:
        text (str): The input text possibly containing HTML tags.

    Returns:
        str: The text with HTML tags removed.
    """
    return re.sub(r'<[^>]+>', '', text)

def remove_urls(text):
    """
    Removes URLs from the input text.

    Args:
        text (str): The input text possibly containing URLs.

    Returns:
        str: The text with URLs removed.
    """
    return re.sub(r'https?://\S+|www\.\S+', '', text)

def remove_emojis(text):
    """
    Removes emojis from the input text.
    Args:
        text (str): The input text possibly containing emojis.
    Returns:
        str: The text with emojis removed.
    """
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002700-\U000027BF"  # Dingbats
        u"\U000024C2-\U0001F251"  # Enclosed characters
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def remove_numbers(text):
    """
    Removes all numbers (Persian and English) from the input text.
    Args:
        text (str): The input text possibly containing numbers.
    Returns:
        str: The text with numbers removed.
    """
    # Remove English and Persian digits
    return re.sub(r'[0-9۰-۹]', '', text)

def handle_special_characters(text):
    """
    Replaces all special characters (except word characters and whitespace) with a space.
    Args:
        text (str): The input text possibly containing special characters.
    Returns:
        str: The text with special characters replaced by spaces.
    """
    import re
    text = re.sub(r'[^\w\s]', ' ', text)
    return text

def normalize_text(text):
    """
    Applies all normalization steps: remove HTML, remove URLs, remove emojis, remove numbers, handle special characters, normalize Arabic chars, and hazm normalization.

    Args:
        text (str): The input text to normalize.

    Returns:
        str: The fully normalized text.
    """
    text = remove_html_tags(text)
    text = remove_urls(text)
    text = remove_emojis(text)
    text = remove_numbers(text)
    text = handle_special_characters(text)
    text = normalize_arabic(text)
    normalizer = hazm.Normalizer()
    text = normalizer.normalize(text)
    return text


