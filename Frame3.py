import tkinter as tk
from utils import validate_single_alpha, validate_single_digit, show_frame

def create_frame3(root, frame2):
    frame3 = tk.Frame(root, bg="lightblue")
    frame3.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame3.valid_words = []

    results_label = tk.Label(frame3, font=("Courier", 20))
    results_label.pack()

    # Labels
    words_label = tk.Label(frame3, font=("Courier", 50), text="Words", bg="lightblue")
    words_label.place(x=50, y=30)

    score_label = tk.Label(frame3, text="Score", font=("Courier", 50), bg="lightblue")
    score_label.place(x=370, y=12, width=300, height=100)

    filter_label = tk.Label(frame3, font=("Courier", 55), text="Filter Category", bg="lightblue")
    filter_label.place(x=820, y=30)

    # Filter Buttons
    Highest_button = tk.Button(frame3, text="Highest Score", font=("Courier", 30, "bold"))
    Highest_button.place(x=820, y=130, width=500, height=70)

    Longest_button = tk.Button(frame3, text="Longest Word", font=("Courier", 30, "bold"))
    Longest_button.place(x=820, y=230, width=500, height=70)

    Shortest_button = tk.Button(frame3, text="Shortest Word", font=("Courier", 30, "bold"))
    Shortest_button.place(x=820, y=330, width=500, height=70)

    letters_button = tk.Button(frame3, text="Number of letters:", font=("Courier", 30, "bold"))
    letters_button.place(x=820, y=430, width=380, height=70)

    vcmd_digit = (root.register(validate_single_digit), '%P')
    letterN_filter = tk.Entry(frame3, font=("Courier", 50), validate="key", validatecommand=vcmd_digit)
    letterN_filter.place(x=1210, y=430, width=110, height=70)

    Contains_button = tk.Button(frame3, text="Contains letter:", font=("Courier", 30, "bold"))
    Contains_button.place(x=820, y=530, width=380, height=70)

    vcmd_alpha = (root.register(validate_single_alpha), '%P')
    letter_filter = tk.Entry(frame3, font=("Courier", 50), validate="key", validatecommand=vcmd_alpha)
    letter_filter.place(x=1210, y=530, width=110, height=70)

    next_button = tk.Button(frame3, text="Next Round", command=lambda: show_frame(frame2), font=("Courier", 30, "bold"))
    next_button.place(x=828, y=700, width=492, height=63)

    # Words Text Box + Scrollbar
    words_text = tk.Text(frame3, font=("Courier", 20, "bold"), wrap="none", state="disabled")
    words_text.place(x=50, y=130, width=300, height=635)

    # Score Text Box + Shared Scrollbar
    score_list = tk.Text(frame3, font=("Courier", 20, "bold"), wrap="none", state="disabled")
    score_scroll = tk.Scrollbar(frame3, command=lambda *args: (score_list.yview(*args), words_text.yview(*args)))
    score_list.config(yscrollcommand=score_scroll.set)
    words_text.config(yscrollcommand=score_scroll.set)
    score_list.place(x=420, y=130, width=300, height=635)
    score_scroll.place(x=720, y=130, width=20, height=635)

    # Sync mouse wheel scrolling
    def on_mousewheel(event):
        score_list.yview_scroll(int(-1*(event.delta/120)), "units")
        words_text.yview_scroll(int(-1*(event.delta/120)), "units")
        return "break"

    score_list.bind("<MouseWheel>", on_mousewheel)
    words_text.bind("<MouseWheel>", on_mousewheel)

    return frame3, letterN_filter, letter_filter, words_text, score_list, next_button