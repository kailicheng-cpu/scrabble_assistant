"""
    A class to calculate Scrabble scores for words.

    Attributes:
        score_system (dict): Maps lowercase letters to their Scrabble point values.
        word_scores (dict): Stores calculated scores for each word.
"""
import time

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
        self.reset()
        for word in words:
            score = 0

            # Loop through each letter in the word (convert to lowercase to match score_system keys)
            for l in word.lower():
                score += self.score_system[l]   # Add the letter's score, based of dictionary
            self.word_scores[word] = score  # Save the total score for this word

        return self.word_scores

    def reset(self):
        self.word_scores = {}

    # 1. Test normal words
    def test_normal_words(self):
        words = ['CAT', 'TAB', 'BUZZ']
        expected = {'CAT': 5, 'TAB': 5, 'BUZZ': 24}
        result = self.calc_score(words)
        print("Normal words test:", result)
        return result == expected

    # 2. Test case-insensitivity not needed as all words most likely will be uppercase, if not will be converted to lowercase

    # 3. Test single-letter words
    def test_single_letters(self):
        words = ['A', 'Z', 'Q']
        expected = {'A': 1, 'Z': 10, 'Q': 10}
        result = self.calc_score(words)
        #print("Single letters test:", result)
        return result == expected

    # 4. Test repeated letters
    def test_repeated_letters(self):
        words = ['AAA', 'ZZZ']
        expected = {'AAA': 3, 'ZZZ': 30}
        result = self.calc_score(words)
        #print("Repeated letters test:", result)
        return result == expected

    # 5. Test empty word
    def test_empty_word(self):
        words = ['']
        expected = {'': 0}
        result = self.calc_score(words)
        #print("Empty word test:", result)
        return result == expected

    # 6. Test empty list
    def test_empty_list(self):
        words = []
        expected = {}
        result = self.calc_score(words)
        #print("Empty list test:", result)
        return result == expected

    # 7. Stress test / performance
    def stress_test(self):
        words = ['CAT', 'TAB', 'BUZZ', 'QUIZ', 'JAZZ', 'AX']
        start_time = time.perf_counter()
        self.calc_score(words)
        end_time = time.perf_counter()
        runtime = end_time - start_time

        return runtime

# Testing Suite
if __name__ == "__main__":      # So that it won’t run when the file is imported
    WS = WordScoring()
    print(WS.calc_score(['CAT', 'TAB', 'BUZZ']))

    print("Running WordScoring Tests...")
    print("Testing Normal words:", WS.test_normal_words())
    print("Testing Single letters:", WS.test_single_letters())
    print("Testing Repeated letters:", WS.test_repeated_letters())
    print("Testing Empty word:", WS.test_empty_word())
    print("Testing Empty list:", WS.test_empty_list())
    print("Stress test runtime:", WS.stress_test)