import tkinter as tk
from utils import letters_or_wild, add_wild

def create_frame2(root, show_frame_func, frame3, frame4):
    frame2 = tk.Frame(root, bg="lightblue")
    frame2.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Labels and Entries
    label2 = tk.Label(frame2, font=("Courier", 60), text="Enter letters:", bg="lightblue")
    label2.place(x=340, y=230)

    score_label = tk.Label(frame2, font=("Courier", 55), text="Score:", bg="lightblue")
    score_label.place(x=30, y=710)

    score_text = tk.Entry(frame2, font=("Courier", 60))
    score_text.place(x=250, y=710, width=380, height=73)

    vcmd = (root.register(letters_or_wild), '%P')
    enter_text = tk.Entry(frame2, font=("Courier", 60), validate='key', validatecommand=vcmd)
    enter_text.place(x=330, y=300, width=600, height=80)

    solve_button = tk.Button(frame2, text="Solve", command=lambda: show_frame_func(frame3), font=("Courier", 50, "bold"))
    solve_button.place(x=500, y=400, width=300, height=100)

    test_button = tk.Button(frame2, text="Word Check", command=lambda: show_frame_func(frame4), font=("Courier", 50, "bold"))
    test_button.place(x=980, y=710, width=400, height=80)

    wild_button = tk.Button(frame2, text="Add\nWild", command=lambda: add_wild(enter_text), font=("Courier", 30, "bold"))
    wild_button.place(x=950, y=300, width=160, height=80)

    return frame2, enter_text, score_text