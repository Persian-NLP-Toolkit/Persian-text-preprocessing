"""
    Author: Alireza Parvaresh
    Email: parvvaresh@gmail.com
    LinkedIn: https://www.linkedin.com/in/parvvaresh/
"""

import hazm
from .remove_stopwords.remove_stopwords import remove_stopwords

lemmatizer = hazm.Lemmatizer()

def lemmatizer(tokens: list) -> list:
    """
    This function lemmatizes a list of tokens using the Hazm library and removes stopwords.

    Parameters:
        tokens (list): A list of Persian tokens.

    Returns:
        list: A list of lemmatized tokens with stopwords removed.
    """
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return remove_stopwords(tokens)