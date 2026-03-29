"""
    A class to calculate Scrabble scores for words.

    Attributes:
        score_system (dict): Maps lowercase letters to their Scrabble point values.
        word_scores (dict): Stores calculated scores for each word.
"""

class WordScoring:
    def __init__(self):
        self.score_system = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
    'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
    'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
        # Dictionary to store the calculated scores for words
        self.word_scores = {}

    def calc_score(self, words):
        """
        Calculate the Scrabble score for a list of words.

        :param words: list(str)
            List of valid words to score
        :return: dict
            A dictionary where keys are words and values are their Scrabble scores.

        Example:
            WS = WordScoring()
            WS.calc_score(['CAT', 'TAB', 'BUZZ'])
            Output: {'CAT': 5, 'TAB': 5, 'BUZZ': 28}
        """
        for word in words:
            score = 0

            # Loop through each letter in the word (convert to lowercase to match score_system keys)
            for l in word.lower():
                score += self.score_system[l]   # Add the letter's score, based of dictionary
            self.word_scores[word] = score  # Save the total score for this word

        return self.word_scores

    def reset(self):
        self.word_scores = {}

WS = WordScoring()
print(WS.calc_score(['CAT', 'TAB', 'BUZZ']))