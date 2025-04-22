"""
    Author: Alireza Parvaresh
    Email: parvvaresh@gmail.com
    LinkedIn: https://www.linkedin.com/in/parvvaresh/
"""
import re

def remove_repeating_chars(text: str) -> str:
    """
    Removes repeating characters from a given Persian text.

    Args:
        text (str): The input text to process.

    Returns:
        str: The text with repeating characters removed.
    """
    return re.sub(r'(.)\1+', r'\1', text)