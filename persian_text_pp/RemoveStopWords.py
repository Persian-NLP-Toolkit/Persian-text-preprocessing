from persian_text_pp.get_stopwords.get_stopwords import get_stopwords_list

def remove_stopwords(tokens: list) -> list:
    """
    Removes stopwords from a list of tokens using a predefined list of Persian stopwords.

    Parameters:
        tokens (list): A list of tokens (words) from which stopwords need to be removed.

    Returns:
        list: A list of tokens with stopwords removed.
    """
    stopwords = get_stopwords_list()
    return [token for token in tokens if token not in stopwords]