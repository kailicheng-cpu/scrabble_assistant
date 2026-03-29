from ComboFinder import ComboFinder
import pytest
import math

class test_combotesting:
    def calc_num_options(tiles):
        sum = 0
        n = len(tiles)
        for i in range(1, n + 1):
            sum += math.comb(n, i) * math.factorial(i)

        print(sum)

    def test_word_finder(self):
        wf = ComboFinder()
        tiles = ["A", "B", "C", "D"]
        result = wf.generate_combo(tiles)

        assert len(result) == test_combotesting.calc_num_options(tiles)


class test_WordFinder:
    def test_load_words(self):
        assert False

    def test_generate_combo(self):
        assert False

    def test_combo_building(self):
        assert False

    def test_reset_generation(self):
        assert False
