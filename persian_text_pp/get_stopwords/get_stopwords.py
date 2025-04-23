import glob  
import os   
import hazm


stop_words_hazm = list(hazm.stopwords_list())



def get_stopwords_list() -> list:
    """
    Retrieves a comprehensive list of Persian stopwords by combining custom stopwords from text files
    in the './persian_stopwords' directory with the default stopwords provided by Hazm.

    Returns:
        list: A unique list of Persian stopwords.
    """
    base_path = os.path.dirname(__file__)

    # Create full path to persian_stopwords/*.txt
    file_list = glob.glob(os.path.join(base_path, 'persian_stopwords', '*.txt'))
    stop_words = []

    # Iterate over each file found in the directory.
    for file_path in file_list:
        with open(file_path) as f:
            stop_words.extend(f.readlines())

    for i in range(len(stop_words)):
        stop_words[i] = stop_words[i].replace('\n', '')

    stop_words.extend(stop_words_hazm)
    return list(set(stop_words))



