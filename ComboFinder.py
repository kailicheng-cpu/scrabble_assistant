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

class ComboFinder:
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


# ------------------------ Testing ------------------------

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

    def num_combos_duplicate(self, tiles):
        self.reset_generation()

        sum = 0
        n = len(tiles)
        self.generate_combo(tiles)

        for i in range(1, n + 1):
            sum += math.comb(n, i) * math.factorial(i)

        if self.num_combos < sum:
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

    def case_sensitivity(self, tiles):
        self.reset_generation()

        self.generate_combo(tiles)

        for i in self.generated_combinations:
            if not i.isupper():
                print(False)
                return
        print(True)


# making sure words are being loaded correctly
combofinder = ComboFinder()
combofinder.load_words()

# TESTING SUITE
'''wordfinder.generate_combo([]) # Output: empty set
wordfinder.reset_generation()

wordfinder.generate_combo(['A']) # Output: {'A'} --> single Value
wordfinder.reset_generation()'''

print("Testing 4 distinct: ", end="")
combofinder.calc_num_combos(['A', 'G', 'L', 'P'])# multiple distinct Values

print("Testing 10 distinct: ", end="")
combofinder.calc_num_combos(['C', 'A' , 'T', 'Z', 'P', 'Q', 'L', 'B', 'M', 'N'])

print("Testing 2 duplicate Values: ", end="")
combofinder.num_combos_duplicate(['A', 'A']) # Output: True --> 2 < 4 {'A', 'AA'} --> Repeated letters will create duplicate combos that the set should remove

print("Testing duplicates with multiple values: ", end="")
combofinder.num_combos_duplicate(['C', 'A' , 'T', 'Z', 'P', 'Q', 'B', 'B', 'N', 'N'])

print("Testing Case Sensitivity: ", end="")
combofinder.case_sensitivity(['c', 'A', 'T']) # Output: True -->{'CAT', 'ACT',...} --> case sensitivity, 'c' should be caplitalized
combofinder.reset_generation()

# Different Characters--> special character(s) used for wild cards later
print("Testing Special Characters: ", end="")
combofinder.generate_combo(['A', '1', '?']) # Just making sure it works the same with special characters
print(combofinder.generated_combinations)

print("Testing runtime for 10 tiles: ", end="")
combofinder.stress_test(['C', 'A' , 'T', 'Z', 'P', 'Q', 'L', 'B', 'M', 'N']) # starts to slow down extreme at 10 tiles

# 11 take too long 3.5min to run, therefore max characters of 10
'''print("Testing runtime for 11 tiles")
wordfinder.stress_test(['C', 'A' , 'T', 'Z', 'P', 'Q', 'L', 'B', 'M', '*','N']) 
wordfinder.reset_generation()'''
