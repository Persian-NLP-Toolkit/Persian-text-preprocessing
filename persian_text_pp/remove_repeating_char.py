"""
    Author: Alireza Parvaresh
    Email: parvvaresh@gmail.com
    LinkedIn: https://www.linkedin.com/in/parvvaresh/
"""
import re

def remove_repeating_char(text):
    """
    This function removes consecutive repeating characters in a string, leaving only a single instance of the character.

    Parameters:
        text (str): The input text where repeating characters need to be removed.

    Returns:
        str: The text with consecutive repeating characters replaced by a single instance.
    """
    # Using a regular expression to replace consecutive repeating characters with a single instance
    return re.sub(r'(.)\1+', r'\1', text)