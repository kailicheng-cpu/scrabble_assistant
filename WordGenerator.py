from ComboFinder import ComboFinder
from WordVerification import WordVerifications

class WordGenerator:
    def __init__(self):
        self.words = None
        self.score = None
        self.CF = ComboFinder()
        self.WV = WordVerifications()

    def doaction(self, tiles):
        self.reset()

        # make Combos
        self.CF.generate_combo(tiles)

        # verify Combos for words

        self.words = self.WV.validate_word(self.CF.get_generated_combos())

        # Calculated and get score for words

        return self.words

    def reset(self):
        self.words = None
        self.score = None
        self.CF.reset_generation()
        self.WV.reset()

WG = WordGenerator()
WG.doaction(['C', 'A', 'T'])