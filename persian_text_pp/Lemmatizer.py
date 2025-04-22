"""
Author: Alireza Parvaresh
Email: parvvaresh@gmail.com
LinkedIn: https://www.linkedin.com/in/parvvaresh/
"""

from hazm import Lemmatizer

# Initialize the Hazm Lemmatizer
lemmatizer = Lemmatizer()


def lemmatize(tokens: list) -> list:
    """
    Lemmatizes a list of Persian tokens using Hazm's Lemmatizer.

    Parameters:
        tokens (list): A list of Persian tokens to be lemmatized.

    Returns:
        list: A list of lemmatized tokens.
    """
    return [lemmatizer.lemmatize(token) for token in tokens]