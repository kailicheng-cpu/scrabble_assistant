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

# -------------------- Testing ----------------------

"""
Manual testing

Test 1: Valid letters
Input: "CAT"
Expected: Input accepted
Actual: Input accepted
Result: PASS

Test 2: Wildcard input

Input: "C*T"
Expected: Input accepted (* allowed)
Actual: Input accepted
Result: PASS

Test 3: Invalid characters

Input: "CAT1"
Expected: Input rejected (numbers not allowed)
Actual: Number not entered
Result: PASS

Test 4: Too many characters

Input: "ABCDEFGHIJK" (11 letters)
Expected: Input limited to 10 characters
Actual: Extra characters not accepted
Result: PASS

Test 5. Empty input

Input: ""
Action: Click Solve
Expected: No crash, empty lists in frame3
Actual: no words displayed
Result: PASS

Test 6: Wildcard input

Input: "C*T"
Action: Click Solve
Expected: Words generated using wildcard
Actual: Words generated correctly
Result: PASS

Test 7: Navigation to Frame 4

Action: Click "Word Check"
Expected: Switch to frame4
Actual: Frame changed correctly
Result: PASS

Test 8: Add wildcard

Input before: "CAT"
Action: Click "Add Wild"
Expected: "CAT*" appears in entry
Actual: "*" added correctly
Result: PASS

Test 9: Input score

Input before: 10
Action: Switch to frame3 then back to frame2
Expected: Score remains on the screen
Actual: 10 is displayed
Result: PASS

"""