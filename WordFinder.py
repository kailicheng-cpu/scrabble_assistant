'''
Loops through the dictionary and collects all playable words

Generates possible letter combinations from the given rack of tiles
Checks which combinations form valid words by comparing them with the dictionary
Returns only real, game-ready words that can actually be made from the input letters

input: Group of letters/tiles from the player's board
output: list of valid playable words

Note:
Use a set for the generated possible combinations, because a set removes duplicate combination of letters
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