
from dictionary_manager import DictionaryManager
from

class WordVerification:
    def __init__(self):
        self.generated_combos = None
        self.verified = []

        self.load_words()

    def load_words(self):
        self.dict_manager = DictionaryManager()
        self.dictionary_words = self.dict_manager.get_word_list()
        #print(self.dictionary_words)

    def load_combos(self):
