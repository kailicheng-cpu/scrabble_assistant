import tkinter as tk
from utils import letters_or_wild

def create_frame4(root, show_frame_func, frame4):
    frame4 = tk.Frame(root, bg="lightblue")
    frame4.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Labels and Entries
    label4 = tk.Label(frame4, font=("Courier", 60), text="Enter word:", bg="lightblue")
    label4.place(x=340, y=230)

    vcmd = (root.register(letters_or_wild), '%P')
    enter_word = tk.Entry(frame4, font=("Courier", 60), validate='key', validatecommand=vcmd)
    enter_word.place(x=330, y=300, width=600, height=80)

    back_button = tk.Button(frame4, text="Back", command=lambda: show_frame_func(frame2), font=("Courier", 50, "bold"))
    back_button.place(x=980, y=710, width=400, height=80)

    check_button = tk.Button(frame4, text="Check word", font=("Courier", 40, "bold"))
    check_button.place(x=500, y=400, width=300, height=100)

    return frame4, enter_word, back_button