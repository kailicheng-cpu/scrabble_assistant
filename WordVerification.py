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

class WordVerifications:
    """
        A class to verify which generated word combinations are valid
        words according to a loaded dictionary.
    """
    def __init__(self, generatedcombos):
        self.dict_manager = None

        self.generated_combos = list(generatedcombos)
        self.verified = []

        self.load_words()

    def load_words(self):
        """Load the word list from DictionaryManager."""
        self.dict_manager = DictionaryManager()
        self.dictionary_words = self.dict_manager.get_word_list() # List of all valid words
        #print(self.dictionary_words)

    def sort_words(self):
        """
        Sort the generated combinations alphabetically.
        This ensures consistency for validation and potential binary search.
        :return: None
        """
        self.generated_combos.sort()

    def validate_word(self):
        """
        Validate each generated combo against the dictionary using binary search.
        :return: list
            List of verified words found in the dictionary.
        """
        self.sort_words()
        combos = self.dictionary_words # Search against the official dictionary

        for i in self.generated_combos:
            high = len(combos) + 1 # Corrected binary search upper bound
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
        print(self.verified)
        return self.verified

    def get_word(self):
        return(self.verified)

if __name__ == "__main__":      # So that it won’t run when the file is imported
    CF = ComboFinder()
    CF.generate_combo(['C', 'A' , 'T']) # --> minimum 2 letter words --> Output: ['ACT', 'AT', 'CAT', 'TA']
    print(CF.get_generated_combos())

    WV = WordVerifications(CF.get_generated_combos())
    WV.validate_word()
