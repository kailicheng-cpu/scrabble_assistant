import tkinter as tk
from utils import letters_or_wild, add_wild, solve
from WordGenerator import WordGenerator

generator = WordGenerator()

def create_frame2(root, show_frame_func, frame3, frame4, words_text, score_list):
    """
    Creates the second frame where the user enters letters to generate Scrabble words.

    Parameters:
\
    root : tk.Tk
        The main Tkinter window.
    show_frame_func : function
        Function used to switch frames (like show_frame).
    frame3 : tk.Frame
        The frame where results (words and scores) are displayed.
    frame4 : tk.Frame
        The frame used for checking individual words.
    words_text : tk.Text
        Text widget from frame3 that displays generated words.
    score_list : tk.Text
        Text widget from frame3 that displays corresponding scores.

    Returns:

    tuple
        (frame2, enter_text, score_text)
        - frame2: the created Tkinter frame for letter entry.
        - enter_text: Entry widget where user types letters.
        - score_text: Entry widget for displaying score (or extra info).

    Description:

    - Sets up frame2 with a light blue background.
    - Adds a large label prompting the user to enter letters.
    - Provides an entry box with validation to allow only letters or wildcards ('*').
    - Includes a "Solve" button to generate valid Scrabble words and update frame3's text widgets.
    - Includes a "Word Check" button to navigate to frame4 for checking individual words.
    - Includes a "Add Wild" button to insert a wildcard into the letter entry.
    """
    frame2 = tk.Frame(root, bg="lightblue")
    frame2.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Labels and entries
    label2 = tk.Label(frame2, font=("Courier", 60), text="Enter letters:", bg="lightblue")
    label2.place(x=340, y=230)

    score_label = tk.Label(frame2, font=("Courier", 55), text="Score:", bg="lightblue")
    score_label.place(x=30, y=710)

    score_text = tk.Entry(frame2, font=("Courier", 60))
    score_text.place(x=250, y=710, width=380, height=73)

    vcmd = (root.register(letters_or_wild), '%P')
    enter_text = tk.Entry(frame2, font=("Courier", 60), validate='key', validatecommand=vcmd)
    enter_text.place(x=330, y=300, width=600, height=80)

    # Solve button
    solve_button = tk.Button(
        frame2,
        text="Solve",
        font=("Courier", 50, "bold"),
        command=lambda: solve(frame3, enter_text.get(), words_text, score_list, generator)
    )
    solve_button.place(x=500, y=400, width=300, height=100)

    # Word Check button
    test_button = tk.Button(
        frame2, 
        text="Word Check", 
        command=lambda: show_frame_func(frame4), 
        font=("Courier", 50, "bold")
    )
    test_button.place(x=980, y=710, width=400, height=80)

    # Add Wildcard button
    wild_button = tk.Button(
        frame2, 
        text="Add\nWild", 
        command=lambda: add_wild(enter_text), 
        font=("Courier", 30, "bold")
    )
    wild_button.place(x=950, y=300, width=160, height=80)

    return frame2, enter_text, score_text