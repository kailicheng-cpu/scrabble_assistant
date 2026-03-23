'''Loops through dictionary and collects playable words
input: Letters (sorted)
return: list of possible words
'''
class WordFinder:
    def __init__(self):
        self.file_name = 'dictionary.txt'
        self.all_word = []

        self.load_words()

    def load_words(self):
        with open(self.file_name, 'r') as file:

            # Reads each line of the file and saves each line as a value in a list
            self.all_words = [line.strip() for line in file]

    def