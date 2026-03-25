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

from dictionary_manager import DictionaryManager

class WordFinder:
    def __init__(self):
        self.dictionary_words = None
        self.generated_combinations = set()

        self.varified_words = []

        self.load_words()

    def load_words(self):
        self.dict_manager = DictionaryManager()
        self.dictionary_words = self.dict_manager.get_word_list()
        print(self.dictionary_words)

    def generate_combo(self, tiles:list):
        tiles = (t.upper() for t in tiles)

        # starting off the recursive method empty
        self.combo_building("", tiles)

        print(self.generated_combinations)

    def combo_building(self, current_combo, remaining_tiles:list):

        #adding the current combo to the set of results if not empty
        if current_combo:
            self.generated_combinations.add(current_combo)

        else:
            for i in range(len(remaining_tiles)):
                letter = remaining_tiles[i]

                new_combo = current_combo + letter
                new_remainder = remaining_tiles[:i]+remaining_tiles[i:]

                self.combo_building(new_combo, new_remainder)


# making sure words are being loaded correctly
wordfinder = WordFinder()
wordfinder.load_words()

wordfinder.generate_combo(['c', 'A', 'T'])