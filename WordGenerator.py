from ComboFinder import ComboFinder
from WordVerification import WordVerifications
from WordScoring import WordScoring

class WordGenerator:
    """
    A class that combines combo generation, word verification, and scoring
    to produce valid Scrabble words and their scores from a set of tiles.
    """
    def __init__(self):
        self.words = None
        self.score = None
        self.CF = ComboFinder()
        self.WV = WordVerifications()
        self.WS = WordScoring()

    def doaction(self, tiles):
        """
        Main method to process a list of tiles:
        1. Reset previous results
        2. Generate all possible letter combinations
        3. Validate combinations to get real words
        4. Calculate Scrabble scores for the valid words

        :param tiles: list(str)
            The letters to use for generating words

        :return:None
        """
        self.reset()

        # make Combos-->Generate all possible letter combinations from tiles
        self.CF.generate_combo(tiles)

        # verify Combos for words-->Validate which combinations are actual words
        self.words = self.WV.validate_word(self.CF.get_generated_combos())

        # Calculate Scrabble scores for valid words
        #score will return a dictionary
        self.score = self.WS.calc_score(self.words)

        #return self.words, self.score

    def get_words(self):
        """
        Return the list of valid words generated.
        """
        return self.words

    def get_score(self):
        """
        Return a dictionary of words and their Scrabble scores.
        """
        return self.score

    def reset(self):
        """
        Reset all internal state when starting new combos of letters
        - Clears stored words and scores
        - Resets all back-end modules
        """
        self.words = None
        self.score = None
        self.CF.reset_generation()
        self.WV.reset()
        self.WS.reset()

WG = WordGenerator()
WG.doaction(['C', 'A', 'T'])
print(WG.get_words(), ', ', WG.get_score())
