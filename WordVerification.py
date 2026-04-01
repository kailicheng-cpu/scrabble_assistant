'''
    Checks which generated words are valid using the dictionary

    Verifies each word combination against a dictionary using **binary search**
    Returns only real, playable words that exist in the dictionary

    Input: List of generated word combinations
    Output: List of verified dictionary words

    Notes:
    - Use a set for generated combinations to remove duplicates, but changed to a list for indexing
    - Use **binary search** instead of linear search for faster lookup
    - Dictionary must be sorted
    - Binary search splits the list in half each time
    - Much faster for large dictionaries (O(log n) vs O(n))

    final binary seach for ALL values in dictionary list --> O(m*log(n))
'''
from DictionaryManager import DictionaryManager
from ComboFinder import ComboFinder
import time

class WordVerifications:
    """
        A class to verify which generated word combinations are valid
        words according to a loaded dictionary.
    """
    def __init__(self):
        self.dict_manager = None

        self.verified = []

        self.load_words()

    def load_words(self):
        """Load the word list from DictionaryManager."""
        self.dict_manager = DictionaryManager()
        self.dictionary_words = self.dict_manager.get_word_list() # List of all valid words
        #print(self.dictionary_words)

    def sort_words(self, word_list):
        """
        Sort the generated combinations alphabetically.
        This ensures consistency for validation and potential binary search.
        :return: None
        """
        word_list.sort()

    def validate_word(self, generatedcombos):
        """
        Validate each generated combo against the dictionary using binary search.
        :return: list
            List of verified words found in the dictionary.
        """
        self.reset()

        generatedcombos = list(generatedcombos)

        self.sort_words(generatedcombos)

        for i in range(len(generatedcombos)):
            generatedcombos[i] = generatedcombos[i].upper()

        combos = self.dictionary_words # Search against the official dictionary

        for i in generatedcombos:
            high = len(combos) - 1 # Corrected binary search upper bound
            low = 0

            while high >= low:
                mid = (high + low) // 2 # Middle index for binary search
                if combos[mid] == i: # Word found in dictionary
                    self.verified.append(combos[mid])
                    break
                elif combos[mid] > i: # Search left half
                    high = mid - 1
                else:
                    low = mid + 1 # Search right half
        #print(self.verified)
        return self.verified

    def get_word(self):
        return(self.verified)

    def reset(self):
        self.verified = []

# ------------------------ Testing ------------------------

    def some_valid(self):
        word = ['CAT', 'ACT', 'C']
        valid = ['ACT', 'CAT']

        checked = self.validate_word(word)
        checked.sort()

        #print(checked)

        if valid == checked:
            return True

        return False

    def all_valid(self):
        word = ['CAT', 'ACT', 'AT']
        valid = ['ACT', 'AT', 'CAT']

        checked = self.validate_word(word)
        checked.sort()

        #print(checked)

        if valid == checked:
            return True

        return False

    def none_valid(self):
        word = ['PZS', 'YPC', 'AV']
        valid = []

        checked = self.validate_word(word)
        checked.sort()

        #print(checked)

        if valid == checked:
            return True

        return False

    def no_words(self):
        word = []
        valid = []

        checked = self.validate_word(word)
        checked.sort()

        # print(checked)

        if valid == checked:
            return True

        return False

    def stress_test(self, combos):

        start_time = time.perf_counter()
        self.validate_word(combos)
        end_time = time.perf_counter()

        runtime = end_time - start_time
        print(runtime)

    def case_sensitivity(self):
        words = ['cat', 'mat']

        check = self.validate_word(words)

        for word in check:
            if not word.isupper():
                return False
        return True


if __name__ == "__main__":      # So that it won’t run when the file is imported

# TESTING SUITE
    CF = ComboFinder()
    CF.generate_combo(['C', 'A' , 'T']) # --> minimum 2 letter words --> Output: ['ACT', 'AT', 'CAT', 'TA']
    print(CF.get_generated_combos())

    WV = WordVerifications()
    print(WV.validate_word(CF.get_generated_combos()))

    print("Testing case sensitivity: ", end="")
    print(WV.case_sensitivity())

    print("Testing some valid and invalid words: ", end="")
    print(WV.some_valid())

    print("Testing all valid words: ", end="")
    print(WV.all_valid())

    print("Testing no valid words: ", end="")
    print(WV.none_valid())

    print("Testing no words: ", end="")
    print(WV.no_words())

    print("Testing runtime for all combinations made with 9 tiles: ")
    combos = CF.generate_combo(['C', 'A', 'T', 'Z', 'P', 'Q', 'L', 'B', 'M'])
    # print(CF.get_generated_combos())
    print('Validating Words...')
    WV.stress_test(CF.get_generated_combos())

    print("Testing runtime for all combinations made with 10 tiles: ")
    combos = CF.generate_combo(['C', 'A' , 'T', 'Z', 'P', 'Q', 'L', 'B', 'M', 'N'])
    #print(CF.get_generated_combos())
    print('Validating Words...')
    WV.stress_test(CF.get_generated_combos())
