from hazm import word_tokenize

def tokenize(text):
    """
    Tokenizes the input text into words using hazm's word_tokenize function.

    Args:
        text (str): The input text to tokenize.

    Returns:
        list: A list of tokenized words.
    """
    return word_tokenize(text)