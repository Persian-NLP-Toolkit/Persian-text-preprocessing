"""
    Author: Alireza Parvaresh
    Email: parvvaresh@gmail.com
    LinkedIn: https://www.linkedin.com/in/parvvaresh/
"""
import string



def remove_punctuations(text: str) -> str:
    """
    This function removes both standard English and Persian punctuations from the input text.

    Parameters:
        text (str): The input text from which punctuations need to be removed.

    Returns:
        str: The text after removing all specified punctuations.
    """

    # Defining Persian-specific punctuation marks
    persian_punctuations = '''`÷×؛#<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
    
    # Combining standard English punctuations with Persian punctuations
    punctuations_list = string.punctuation + persian_punctuations

    # Creating a translation table to map punctuations to None
    translator = str.maketrans('', '', punctuations_list)

    # Using translate to remove all punctuations from the text
    return text.translate(translator)