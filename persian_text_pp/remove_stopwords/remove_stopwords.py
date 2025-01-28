import glob  
import os    

# Define a class that will handle removing stopwords.
class remove_stopwords:
    def __init__(self) -> None:
        file_list = glob.glob('./persian_stopwords' + '/*.txt')

        self.stop_words = []

        # Iterate over each file found in the directory.
        for file_path in file_list:
            with open(file_path) as f:
                self.stop_words.extend(f.readlines())

        for i in range(len(self.stop_words)):
            self.stop_words[i] = self.stop_words[i].replace('\n', '')

    # Method to remove stopwords from a list of tokens.
    def remove_stopwords(self, tokens: list) -> list:
        tokens = [token for token in tokens if token not in self.stop_words]
        return tokens
