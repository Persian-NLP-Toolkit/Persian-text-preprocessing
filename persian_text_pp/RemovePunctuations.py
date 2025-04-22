"""
Author: Alireza Parvaresh
Email: parvvaresh@gmail.com
LinkedIn: https://www.linkedin.com/in/parvvaresh/
"""

import string

def remove_punctuations(text: str) -> str:
    """
    Removes both standard English and Persian punctuations from the input text.

    Parameters:
        text (str): The input text from which punctuations need to be removed.

    Returns:
        str: The text after removing all specified punctuations.
    """
    persian_punctuations = '''`÷×؛#<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
    punctuations_list = string.punctuation + persian_punctuations
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)