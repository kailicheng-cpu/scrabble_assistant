
class DictionaryManager:
    def __init__(self):
        self.file_name = 'dictionary.txt'
        self.word_list = []

        self.load_dictionary()

    def load_dictionary(self):
        '''
        Read each line from the dictionary file, remove extra whitespace and store all words in a list
        :param filename: The name of the dictionary file to read from
        :return: A list of cleaned words from the file
        '''
        with open(self.file_name, 'r') as file:

            # Reads each line of the file and saves each line as a value in a list
            for line in file:
                self.word_list.append(line.strip())

    def get_word_list(self):
        '''
        Returns list of valid words from dictionary
        :return: list
        The word list requested
        '''
        return self.word_list

dictionarymanager = DictionaryManager()
#print(dictionarymanager.get_word_list())