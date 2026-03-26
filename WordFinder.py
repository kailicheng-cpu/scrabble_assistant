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
import math # comb
import time

class WordFinder:
    def __init__(self):
        self.dictionary_words = None
        self.generated_combinations = set()
        self.num_combos = 0
        self.varified_words = []

        self.load_words()

    def load_words(self):
        self.dict_manager = DictionaryManager()
        self.dictionary_words = self.dict_manager.get_word_list()
        # print(self.dictionary_words)

    def generate_combo(self, tiles:list):
        '''
        Will result in a set of all possible combinations using the given tiles
        :param tiles: list
            players tiles/letters that they want to create words using
        :return: None
        '''
        for t in range(len(tiles)):
            tiles[t] = tiles[t].upper()

        # starting off the recursive method empty
        self.combo_building("", tiles)

        # Output all generated combinations
        #print(self.generated_combinations)

        #print(len(self.generated_combinations))

        self.num_combos = len(self.generated_combinations)

    def combo_building(self, current_combo, remaining_tiles:list):
        '''
        Recursively build all possible letter/tile combinations
        As long as the current combo is not empty it will continue to add the current combo to the set
        until there are no longer any remaining tiles

        At each step:
        - Add the current combination to the set (if not empty)
        - Try adding each remaining letter to the combination
        - Remove that letter from the pool and recurse

        :param current_combo: str
            previous build word or empty string, to add letters to continue building combinations
        :param remaining_tiles:
        :return:
        '''
        #adding the current combo to set (ignored if current is empty)
        if current_combo:
            self.generated_combinations.add(current_combo)

        for i in range(len(remaining_tiles)):

            # Choose a letter at index i
            letter = remaining_tiles[i]
            #print(letter) # debugging: shows which letter is chosen--> based on i (the for loop)

            # Build a new combination by adding the chosen letter
            new_combo = current_combo + letter
            #print(new_combo)  # debugging: shows which combo is made

            new_remainder = remaining_tiles[:i]+remaining_tiles[i+1:]
            #print(new_remainder) # debugging: shows which letter are remaining--> therefore used in the recursive portion

            # Recursive call:
            # Continue building using the updated combo and remaining letters
            self.combo_building(new_combo, new_remainder)

    def reset_generation(self):
        '''
        Will empty the list of previously created combinations
        :return: None
        '''
        self.generated_combinations = set()
        self.varified_words = []

    def calc_num_combos(self, tiles):
        self.reset_generation()

        sum = 0
        n = len(tiles)
        self.generate_combo(tiles)

        for i in range(1, n+1):
            sum+= math.comb(n, i)*math.factorial(i)

        if self.num_combos == sum:
            print(True)
        else:
            print(False)

    def stress_test(self, tiles):
        self.reset_generation()

        start_time = time.perf_counter()
        self.generate_combo(tiles)
        end_time = time.perf_counter()

        runtime = end_time - start_time
        print(runtime)


# making sure words are being loaded correctly
wordfinder = WordFinder()
wordfinder.load_words()

# TESTING SUITE
'''wordfinder.generate_combo([]) # Output: empty set
wordfinder.reset_generation()

wordfinder.generate_combo(['A']) # Output: {'A'} --> single Value
wordfinder.reset_generation()'''

print("Testing 4 distinct: ", end="")
wordfinder.calc_num_combos(['A', 'G', 'L', 'P'])# multiple distinct Values

# starts to slow down extreme at 10 tiles, 11 take too long 3.5min to run, therefore max characters of 10
'''print("Testing runtime for 11 tiles")
wordfinder.stress_test(['C', 'A' , 'T', 'Z', 'P', 'Q', 'L', 'B', 'M', '*','N']) 
wordfinder.reset_generation()'''

#wordfinder.calc_num_combos(['A', 'A']) # Output: {'A', 'AA'} --> Repeated letters will create duplicate combos that the set should remove
#wordfinder.reset_generation()

'''wordfinder.generate_combo(['A', ''])

wordfinder.generate_combo(['A', 'A']) # Output: {'A', 'AA'} --> Repeated letters will create duplicate combos that the set should remove
wordfinder.reset_generation()

wordfinder.generate_combo(['C', 'A' , 'T', 'Z', 'P', 'Q', 'L'])
wordfinder.reset_generation()

wordfinder.generate_combo(['c', 'A', 'T']) # Output: {'CAT', 'ACT',...} --> case sensitivity, 'c' should be caplitalized
wordfinder.reset_generation()

wordfinder.generate_combo(['A', '1', '?']) # Different Characters--> special character(s) used for wild cards laterwordfinder.reset_generation()
wordfinder.reset_generation()'''
