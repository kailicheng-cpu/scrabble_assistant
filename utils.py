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