import tkinter as tk
from utils import letters_or_wild, check_word

def create_frame4(root, show_frame_func, frame4):
    """
    Creates Frame 4 of the Scrabble Assistant GUI.

    Parameters:
    - root: The main Tkinter window.
    - show_frame_func: Function used to switch between frames.
    - frame4: Placeholder for the frame object (returned for later use).

    Returns:
    - frame4: The frame object for Frame 4.
    - enter_word: Tkinter Entry widget for word input.
    - back_button: Tkinter Button widget to return to the previous frame.

    Description:
    - This frame allows the user to:
    - Enter a word in an input box.
    - Check if the word exists in the dictionary.
    - See the result displayed as "Yes" or "No".
    - Navigate back to the previous frame.
    """
    
    # Main Frame 
    frame4 = tk.Frame(root, bg="lightblue")
    frame4.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Labels
    label4 = tk.Label(frame4, font=("Courier", 60), text="Enter word:", bg="lightblue")
    label4.place(x=340, y=230)

    result_label = tk.Label(frame4, font=("Courier", 60), text=" ", bg="lightblue")
    result_label.place(x=940, y=300)

    # Entry 
    vcmd = (root.register(letters_or_wild), '%P')
    enter_word = tk.Entry(frame4, font=("Courier", 60), validate='key', validatecommand=vcmd)
    enter_word.place(x=330, y=300, width=600, height=80)

    # Buttons 
    back_button = tk.Button(
        frame4, text="Back", font=("Courier", 50, "bold"),
        command=lambda: show_frame_func(frame2)
    )
    back_button.place(x=980, y=710, width=400, height=80)

    check_button = tk.Button(
        frame4, text="Check word", font=("Courier", 40, "bold"),
        command=lambda: check_word(enter_word.get(), result_label)
    )
    check_button.place(x=500, y=400, width=300, height=100)

    # Return Widgets 
    return frame4, enter_word, back_button