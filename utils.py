import tkinter as tk

# Frame switching
def show_frame(frame):
    frame.tkraise()

# Add wildcard to entry
def add_wild(entry_widget):
    entry_widget.insert(tk.END, "*")

# Validation functions
def validate_single_alpha(P):
    return len(P) <= 1 and (P.isalpha() or P == "")

def validate_single_digit(P):
    return len(P) <= 1 and (P.isdigit() or P == "")

def letters_or_wild(P):
    return len(P) <= 10 and all(c.isalpha() or c == '*' for c in P)

def solve(frame3, tiles, words_text, score_list, generator):
    # 1. Generate valid words and scores
    valid_words, scores = generator.doaction(list(tiles))
    
    # 2. Store them in the generator so other frames can access
    generator.words = valid_words
    generator.score = scores
    
    # 3. Raise frame3
    frame3.tkraise()
    
    # 4. Update the words_text box in frame3
    words_text.config(state="normal")
    words_text.delete("1.0", "end")  # clear old words
    for word in generator.words:
        words_text.insert("end", word + "\n")
    words_text.config(state="disabled")

    score_list.config(state="normal")
    score_list.delete("1.0", "end")
    for word in generator.words:
        score = generator.score[word]  # get score for this word
        score_list.insert("end", f"{score}\n")
    score_list.config(state="disabled")

def check_word(word, result_label):
    with open("dictionary.txt", "r") as file:
        word_list = [line.strip().upper() for line in file]

    if word.upper() in word_list:
        result_label.config(text="Yes")
    else:
        result_label.config(text="No")

def update_highest_score(word_filter, words_text, score_list):
    
    filtered_words, filtered_scores = word_filter.highest_score()
    
    words_text.config(state="normal")
    words_text.delete("1.0", "end")
    
    score_list.config(state="normal")
    score_list.delete("1.0", "end")
    
    for word in filtered_words:
        words_text.insert("end", word + "\n")
        score_list.insert("end", str(filtered_scores[word]) + "\n")
    
    words_text.config(state="disabled")
    score_list.config(state="disabled")

def update_longest_word(word_filter, words_text, score_list):
    
    filtered_words, filtered_scores = word_filter.longest_word()
    
    words_text.config(state="normal")
    words_text.delete("1.0", "end")
    
    score_list.config(state="normal")
    score_list.delete("1.0", "end")
    
    for word in filtered_words:
        words_text.insert("end", word + "\n")
        score_list.insert("end", str(filtered_scores[word]) + "\n")
    
    words_text.config(state="disabled")
    score_list.config(state="disabled")

def update_shortest_word(word_filter, words_text, score_list):
    
    filtered_words, filtered_scores = word_filter.shortest_word()
    
    words_text.config(state="normal")
    words_text.delete("1.0", "end")
    
    score_list.config(state="normal")
    score_list.delete("1.0", "end")
    
    for word in filtered_words:
        words_text.insert("end", word + "\n")
        score_list.insert("end", str(filtered_scores[word]) + "\n")
    
    words_text.config(state="disabled")
    score_list.config(state="disabled")

def update_contains_letter(word_filter, words_text, score_list, letter):
    
    filtered_words, filtered_scores = word_filter.contains_letter(letter)
    
    words_text.config(state="normal")
    words_text.delete("1.0", "end")
    
    score_list.config(state="normal")
    score_list.delete("1.0", "end")
    
    for word in filtered_words:
        words_text.insert("end", word + "\n")
        score_list.insert("end", str(filtered_scores[word]) + "\n")
    
    words_text.config(state="disabled")
    score_list.config(state="disabled")

def update_word_length(word_filter, words_text, score_list, length):
    
    filtered_words, filtered_scores = word_filter.word_length(int(length))
        

    print(length)

    words_text.config(state="normal")
    words_text.delete("1.0", "end")
        
    score_list.config(state="normal")
    score_list.delete("1.0", "end")
        
    for word in filtered_words:
        words_text.insert("end", word + "\n")
        score_list.insert("end", str(filtered_scores[word]) + "\n")
        
    words_text.config(state="disabled")
    score_list.config(state="disabled")