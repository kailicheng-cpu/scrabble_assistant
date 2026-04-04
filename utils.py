import tkinter as tk
import time

# Frame management
def show_frame(frame):
    """Bring a given frame to the front so it becomes visible."""
    frame.tkraise()

def add_wild(entry_widget):
    """Insert a '*' wildcard at the end of an Entry widget."""
    entry_widget.insert(tk.END, "*")

# Validation functions for Entry widgets
def validate_single_alpha(P):
    """Allow only one alphabetical character or empty input."""
    return len(P) <= 1 and (P.isalpha() or P == "")

def validate_single_digit(P):
    """Allow only one digit or empty input."""
    return len(P) <= 1 and (P.isdigit() or P == "")

def letters_or_wild(P):
    """Allow up to 10 characters, letters or '*' only."""
    return len(P) <= 10 and all(c.isalpha() or c == '*' for c in P)

# Word generation and GUI update
def solve(frame3, tiles, words_text, score_list, generator):
    """
    Generate valid Scrabble words and scores from given tiles, update
    frame3, and display results in the words and score Text widgets.
    """
    valid_words, scores = generator.doaction(list(tiles))
    generator.words = valid_words
    generator.score = scores
    frame3.tkraise()

    # Update words display
    words_text.config(state="normal")
    words_text.delete("1.0", "end")
    for word in generator.words:
        words_text.insert("end", word + "\n")
    words_text.config(state="disabled")

    # Update scores display
    score_list.config(state="normal")
    score_list.delete("1.0", "end")
    for word in generator.words:
        score_list.insert("end", f"{generator.score[word]}\n")
    score_list.config(state="disabled")

# Dictionary check
def check_word(word, result_label):
    """Check if a word exists in dictionary.txt and update a label."""
    with open("dictionary.txt", "r") as file:
        word_list = [line.strip().upper() for line in file]

    if word.upper() in word_list:
        result_label.config(text="Yes")
    else:
        result_label.config(text="No")

# Word filtering updates
def update_highest_score(word_filter, words_text, score_list):
    """Update Text widgets with words that have the highest score."""
    filtered_words, filtered_scores = word_filter.highest_score()
    words_text.config(state="normal"); words_text.delete("1.0", "end")
    score_list.config(state="normal"); score_list.delete("1.0", "end")
    for word in filtered_words:
        words_text.insert("end", word + "\n")
        score_list.insert("end", str(filtered_scores[word]) + "\n")
    words_text.config(state="disabled"); score_list.config(state="disabled")

def update_longest_word(word_filter, words_text, score_list):
    """Update Text widgets with the longest words."""
    filtered_words, filtered_scores = word_filter.longest_word()
    words_text.config(state="normal"); words_text.delete("1.0", "end")
    score_list.config(state="normal"); score_list.delete("1.0", "end")
    for word in filtered_words:
        words_text.insert("end", word + "\n")
        score_list.insert("end", str(filtered_scores[word]) + "\n")
    words_text.config(state="disabled"); score_list.config(state="disabled")

def update_shortest_word(word_filter, words_text, score_list):
    """Update Text widgets with the shortest words."""
    filtered_words, filtered_scores = word_filter.shortest_word()
    words_text.config(state="normal"); words_text.delete("1.0", "end")
    score_list.config(state="normal"); score_list.delete("1.0", "end")
    for word in filtered_words:
        words_text.insert("end", word + "\n")
        score_list.insert("end", str(filtered_scores[word]) + "\n")
    words_text.config(state="disabled"); score_list.config(state="disabled")

def update_contains_letter(word_filter, words_text, score_list, letter):
    """Update Text widgets with words containing a specific letter."""
    filtered_words, filtered_scores = word_filter.contains_letter(letter)
    words_text.config(state="normal"); words_text.delete("1.0", "end")
    score_list.config(state="normal"); score_list.delete("1.0", "end")
    for word in filtered_words:
        words_text.insert("end", word + "\n")
        score_list.insert("end", str(filtered_scores[word]) + "\n")
    words_text.config(state="disabled"); score_list.config(state="disabled")

def update_word_length(word_filter, words_text, score_list, length):
    """Update Text widgets with words of a specific length."""
    filtered_words, filtered_scores = word_filter.word_length(int(length))

    words_text.config(state="normal"); words_text.delete("1.0", "end")
    score_list.config(state="normal"); score_list.delete("1.0", "end")
    for word in filtered_words:
        words_text.insert("end", word + "\n")
        score_list.insert("end", str(filtered_scores[word]) + "\n")
    words_text.config(state="disabled"); score_list.config(state="disabled")

# -------------------- Testing ----------------------

# Mock label
class MockLabel:
    def __init__(self):
        self.text = ""
    def config(self, text):
        self.text = text


# -------- Tests --------
def test_check_word_exists(word):
    label = MockLabel()
    check_word(word, label)
    return label.text == "Yes"

def test_check_word_not_exists(word):
    label = MockLabel()
    check_word(word, label)
    return label.text == "No"

def test_check_word_case(word):
    label = MockLabel()
    check_word(word, label)
    return label.text == "Yes"


# -------- Test Data --------
testing_words = [
    ("HELLO", True),     # should exist
    ("d", False),        # probably not a valid word
    ("CAT", True),
    ("elephant", True),
    ("hdbfai", False),
    ("", False),
    ("tOwEr", True)      # case test
]


# -------- Runner --------
def run_tests():
    print("Running check_word tests...\n")
    
    start_total = time.time()
    passed = 0

    for word, should_exist in testing_words:
        start = time.time()
        
        label = MockLabel()
        check_word(word, label)
        
        result = (label.text == "Yes")
        end = time.time()

        runtime = round((end - start) * 1000, 3)

        if result == should_exist:
            print(f"[PASS] {word} → {label.text} ({runtime} ms)")
            passed += 1
        else:
            print(f"[FAIL] {word} → got {label.text}, expected {'Yes' if should_exist else 'No'} ({runtime} ms)")

    total_time = round((time.time() - start_total) * 1000, 3)

    print(f"\n{passed}/{len(testing_words)} tests passed")
    print(f"Total runtime: {total_time} ms")


# Run
run_tests()