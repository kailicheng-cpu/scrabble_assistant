"""
WordFilter Module

This module provides the WordFilter class which allows filtering
generated Scrabble words based on various conditions, such as:
- Highest score
- Longest word
- Shortest word
- Word length
- Contains specific letter

It works with the WordGenerator class which generates
words and their scores from a set of letters.
"""
from WordGenerator import WordGenerator
import time

class WordFilter:
    """A class for filtering words based on different conditions."""
    def __init__(self, wordgenerationClass):
        self.word_gen_class = wordgenerationClass
        self.all_word = None
        self.all_scores = None

        self.filtered_word = []
        self.filtered_score = {}

    def reset(self):
        """
        Resets the filter by retrieving all words and scores
        from the WordGenerator instance. Clears previous filter results.
        """
        self.all_word = self.word_gen_class.get_words()
        #print(self.all_word)
        self.all_scores = self.word_gen_class.get_score()
        #print(self.all_scores)
        self.filtered_word = []
        self.filtered_score = {}

    def highest_score(self):
        """
        Filters words to return only those with the highest score.

        :return: tuple
            list of highest scoring words, dict of word:score
        """
        self.reset()

        max_score = max(self.all_scores.values())

        for word, score in self.all_scores.items():
            if score == max_score:
                self.filtered_word.append(word)
                self.filtered_score.update({word: score})

        return self.filtered_word, self.filtered_score

    def word_length(self, length):
        """
        Filters words by a specific length.

        :param length: int
            The desired word length

        :return: tuple
            list of words with specified length, dict of word:score
        """
        self.reset()

        for word, score in self.all_scores.items():
            if len(word) == length:
                self.filtered_word.append(word)
                self.filtered_score.update({word: score})

        return self.filtered_word, self.filtered_score

    def longest_word(self):
        """
        Filters to find the longest word(s).

        :return: tuple
            list of longest words, dict of word:score
        """
        self.reset()

        max_length = max(len(word) for word in self.all_word)

        return self.word_length(max_length)

    def shortest_word(self):
        """
        Filters to find the shortest word(s)

        :return: tuple
            list of shortest words, dict of word:score
        """
        self.reset()

        min_length = min(len(word) for word in self.all_word)

        return self.word_length(min_length)

    def contains_letter(self, letter):
        """
        Filters words containing a specific letter

        :param letter: str
            The letter to search for in words

        :return: tuple
            list of shortest words, dict of word:score
        """
        self.reset()

        letter = letter.strip().upper()

        for word, score in self.all_scores.items():
            if letter in word:
                self.filtered_word.append(word)
                self.filtered_score.update({word: score})

        return self.filtered_word, self.filtered_score

# ------------------------ Testing ------------------------

# 1. Test highest score filter
    def test_highest_score(self):
        words, scores = self.highest_score()
        max_score = max(self.all_scores.values())
        for score in scores.values():
            if score != max_score:
                return False
        return True

    # 2. Test longest word filter
    def test_longest_word(self):
        words, scores = self.longest_word()
        max_length = max(len(word) for word in self.all_word)
        for word in words:
            if len(word) != max_length:
                return False
        return True

    # 3. Test shortest word filter
    def test_shortest_word(self):
        words, scores = self.shortest_word()
        min_length = min(len(word) for word in self.all_word)
        for word in words:
            if len(word) != min_length:
                return False
        return True

    # 4. Test word length filter
    def test_word_length(self, length):
        words, scores = self.word_length(length)
        for word in words:
            if len(word) != length:
                return False
        return True

    # 5. Test contains letter filter
    def test_contains_letter(self, letter):
        words, scores = self.contains_letter(letter)
        letter = letter.upper()
        for word in words:
            if letter not in word:
                return False
        return True

    # 6. Stress test / performance check
    def stress_test(self):
        start_time = time.perf_counter()
        self.highest_score()
        self.longest_word()
        self.shortest_word()
        self.test_word_length(4)
        self.test_contains_letter('x')
        end_time = time.perf_counter()
        runtime = end_time - start_time
        return runtime

# Testing Suite

if __name__ == "__main__":
    WG= WordGenerator()
    WG.doaction(['a','b','n', 'l', 'y', 'z', 'e', 'x', 'p', 'o'])
    #print(WG.doaction(['a','a','n', 'l', 'y', 'z', 'e', 'x', 'p', 'o']))

    WF = WordFilter(WG)
    print('Testing Highest Scored:', WF.test_highest_score())
    print('Testing Longest Words: ', WF.test_longest_word())
    print('Testing Shortest Words: ', WF.test_shortest_word())
    print('Testing Word Length of 4: ',WF.test_word_length(4))
    print('Testing for Words that contain letter x: ', WF.test_contains_letter('x'))
    print('Testing Runtime all word made with 10 letters: ', WF.stress_test())
    # runtime for all filtering methods of 10 unique characters = 6.66...e-05, very fast and efficient filtering methods