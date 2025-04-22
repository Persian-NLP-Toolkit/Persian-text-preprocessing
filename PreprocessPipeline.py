from persian_text_pp.FarsiLanguageRecognition import is_farsi
from persian_text_pp.Normalize import normalize_persian
from persian_text_pp.RemoveDiacritics import remove_diacritics
from persian_text_pp.RemovePunctuations import remove_punctuations
from persian_text_pp.RemoveRepeatingChar import remove_repeating_chars
from persian_text_pp.RemoveStopWords import remove_stopwords
from persian_text_pp.Tokenize import tokenize
from persian_text_pp.Informal2Formal import informal2formal
from persian_text_pp.Lemmatizer import lemmatize

def preprocess_pipeline(
    text,
    unify_chars=True,
    refine_punc_spacing=True,
    remove_html=False,
    replace_email_with="<EMAIL>",
    replace_number_with=None,
    replace_url_with="",
    replace_mobile_number_with=None,
    replace_emoji_with=None,
    replace_home_number_with=None,
):
    """
    Preprocesses Persian text through all standard steps and returns tokens.

    Steps applied (in order):
      1. Detect Farsi language
      2. Normalize text using normalize_persian with customizable options
      3. Remove diacritics
      4. Remove punctuation
      5. Remove repeating characters
      6. Convert informal to formal
      7. Tokenize
      8. Remove stopwords
      9. Lemmatize

    Args:
        text (str): The input Persian text to preprocess.
        unify_chars (bool): Whether to unify similar characters during normalization.
        refine_punc_spacing (bool): Whether to refine punctuation spacing.
        remove_html (bool): Whether to strip HTML tags.
        replace_email_with (str): Replacement for email addresses.
        replace_number_with (str or None): Replacement for numbers.
        replace_url_with (str): Replacement for URLs.
        replace_mobile_number_with (str or None): Replacement for mobile numbers.
        replace_emoji_with (str or None): Replacement for emojis.
        replace_home_number_with (str or None): Replacement for home phone numbers.

    Returns:
        list: The preprocessed tokens.
    """
    # Step 1: Detect if the text is Persian
    if not is_farsi(text):
        raise ValueError("The input text is not in Persian.")

    # Step 2: Normalize the text with detailed options
    text = normalize_persian(
        text,
        unify_chars=unify_chars,
        refine_punc_spacing=refine_punc_spacing,
        remove_html=remove_html,
        replace_email_with=replace_email_with,
        replace_number_with=replace_number_with,
        replace_url_with=replace_url_with,
        replace_mobile_number_with=replace_mobile_number_with,
        replace_emoji_with=replace_emoji_with,
        replace_home_number_with=replace_home_number_with,
    )

    # Step 3: Remove diacritics
    text = remove_diacritics(text)

    # Step 4: Remove punctuation
    text = remove_punctuations(text)

    # Step 5: Remove repeating characters
    text = remove_repeating_chars(text)

    # Step 6: Convert informal text to formal
    #text = informal2formal(text)

    # Step 7: Tokenize the text
    tokens = tokenize(text)

    # Step 8: Remove stopwords (operates on tokens)
    tokens = remove_stopwords(tokens)

    # Step 9: Lemmatize (operates on tokens)
    tokens = lemmatize(tokens)

    return tokens


# Example usage 
# text = "سلام!لطفاً ایمیل test@example.com و شماره ۱۲۳۴۵۶ را بررسی کن :)"
# # Execute pipeline with explicit parameters (no defaults)
# tokens = preprocess_pipeline(
#     text,
#     unify_chars=False,
#     refine_punc_spacing=False,
#     remove_html=True,
#     replace_email_with="[]",
#     replace_number_with="<>",
#     replace_url_with="<>",
#     replace_mobile_number_with="<>",
#     replace_emoji_with="<>",
#     replace_home_number_with="<>"
# )
# print(tokens)
