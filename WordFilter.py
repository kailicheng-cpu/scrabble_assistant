'''
Class for all the filtering conditions
'''
from WordGenerator import WordGenerator

class WordFilter:
    def __init__(self, wordgenerationClass):
        self.word_gen_class = wordgenerationClass
        self.all_word = None
        self.all_scores = None

        self.filtered_word = []
        self.filtered_score = {}

    def reset(self):
        self.all_word = self.word_gen_class.get_words()
        #print(self.all_word)
        self.all_scores = self.word_gen_class.get_score()
        #print(self.all_scores)
        self.filtered_word = []
        self.filtered_score = {}

    def highest_score(self):
        self.reset()

        max_score = max(self.all_scores.values())

        for word, score in self.all_scores.items():
            if score == max_score:
                self.filtered_word.append(word)
                self.filtered_score.update({word: score})

        return self.filtered_word, self.filtered_score

    def word_length(self, length):
        self.reset()

        for word, score in self.all_scores.items():
            if len(word) == length:
                self.filtered_word.append(word)
                self.filtered_score.update({word: score})

        return self.filtered_word, self.filtered_score

    def longest_word(self):
        self.reset()

        max_length = max(len(word) for word in self.all_word)

        return self.word_length(max_length)

    def shortest_word(self):
        self.reset()

        min_length = min(len(word) for word in self.all_word)

        return self.word_length(min_length)

    def contains_letter(self, letter):
        self.reset()

        letter = letter.strip().upper()

        for word, score in self.all_scores.items():
            if letter in word:
                self.filtered_word.append(word)
                self.filtered_score.update({word: score})

        return self.filtered_word, self.filtered_score

WG= WordGenerator()
print(WG.doaction(['a','a','n', 'l', 'y', 'z', 'e', 'x']))

WF = WordFilter(WG)
print('highest scored', WF.highest_score())
print('')
print('lonest words', WF.longest_word())
print('')
print('shortest words', WF.shortest_word())
print('')
print('word length of 4',WF.word_length(4))
print('')
print('words that contain letter x', WF.contains_letter('x'))