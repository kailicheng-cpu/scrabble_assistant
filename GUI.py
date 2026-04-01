import tkinter as tk

def show_frame(frame):
    frame.tkraise()

def add_wild():
    enter_text.insert(tk.END, "*")

root = tk.Tk()
root.geometry("1400x800") 

score = 0

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# ----------------- Frame 1 -----------------
frame1 = tk.Frame(root, bg="lightblue")
frame1.place(x=0, y=0, width=1400, height=800)  # full window

# Title label
title1 = tk.Label(frame1, text="Scrabble\nAssistant", font=("Courier", 120), bg="lightblue")
title1.place(x=380, y=130)  # replicates padx=50, pady=(130,0)

# Start button
start_button = tk.Button(frame1, text="START", command=lambda: show_frame(frame2), font=("Courier", 90, "bold"), bg="white", fg="black")
start_button.place(x=420, y=430, width=560, height=200)  # replicates grid+padx=420, pady=(120,120)


# ----------------- Frame 2 -----------------
frame2 = tk.Frame(root, bg="lightblue")
frame2.place(relx=0, rely=0, relwidth=1, relheight=1)

# Label "Enter letters:"
label2 = tk.Label(frame2, font=("Courier", 60), text="Enter letters:", bg="lightblue")
label2.place(x=340, y=230)  # original padx=(220, 400), pady=(200, 0)

# Score label
score_label = tk.Label(frame2, font=("Courier", 55), text="Score:", bg="lightblue")
score_label.place(x=30, y=710)  # padx=(0, 1130), pady=(450, 20)

# Score Entry
score_text = tk.Entry(frame2, font=("Courier", 60))
score_text.place(x=250, y=710, width=380, height=73)  # match grid spacing

# Function for validation
def letters_or_wild(P):
    return len(P) <= 10 and all(c.isalpha() or c == '*' for c in P)

vcmd = (root.register(letters_or_wild), '%P')

# Entry for letters
enter_text = tk.Entry(frame2, font=("Courier", 60), validate='key', validatecommand=vcmd)
enter_text.place(x=330, y=300, width=600, height=80)  # original padx=350, pady=(10,430)

# Solve button
solve_button = tk.Button(frame2, text="Solve", command=lambda: show_frame(frame3), font=("Courier", 50, "bold"))
solve_button.place(x=500, y=400, width=300, height=100)  # original padx=(500,500), pady=(110,360)

# Wild button
wild_button = tk.Button(frame2, text="Add\nWild", command=add_wild, font=("Courier", 30, "bold"))
wild_button.place(x=950, y=300, width=160, height=80)  # original padx=(1065,230), pady=(10,430)

# ----------------- Frame 3 -----------------
frame3 = tk.Frame(root, bg="lightblue")
frame3.place(relx=0, rely=0, relwidth=1, relheight=1)

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

def validate_single_digit(P):
    return len(P) <= 1 and (P.isdigit() or P == "")

# Register the function with Tkinter
vcmd_letterN = (root.register(validate_single_digit), '%P')

# Create the Entry with validation
letterN_filter = tk.Entry(frame3, font=("Courier", 50),
                          validate="key", validatecommand=vcmd_letterN)

letterN_filter.place(x=1210, y=430, width=110, height=70)

Contains_button = tk.Button(frame3, text="Contains letter:", font=("Courier", 30, "bold"))
Contains_button.place(x=820, y=530, width=380, height=70)

def validate_single_alpha(P):
    return len(P) <= 1 and (P.isalpha() or P == "")

# Register the function with Tkinter
vcmd_letter = (root.register(validate_single_alpha), '%P')

# Create the Entry with validation
letter_filter = tk.Entry(frame3, font=("Courier", 50),
                         validate="key", validatecommand=vcmd_letter)
letter_filter.place(x=1210, y=530, width=110, height=70)

next_button = tk.Button(frame3, text="Next Round", command=lambda: show_frame(frame2), font=("Courier", 30, "bold"))
next_button.place(x=828, y=700, width=492, height=63)

# Words Text Box + Scrollbar
words_text = tk.Text(frame3, font=("Courier", 20, "bold"), wrap="none", state="disabled")
words_scroll = tk.Scrollbar(frame3, command=words_text.yview)
words_text.config(yscrollcommand=words_scroll.set)
words_text.place(x=50, y=130, width=300, height=635)
words_scroll.place(x=350, y=130, width=20, height=635)

# Score Text Box + Shared Scrollbar
score_text = tk.Text(frame3, font=("Courier", 20, "bold"), wrap="none", state="disabled")
score_scroll = tk.Scrollbar(frame3, command=lambda *args: (score_text.yview(*args), words_text.yview(*args)))
score_text.config(yscrollcommand=score_scroll.set)
words_text.config(yscrollcommand=score_scroll.set)
score_text.place(x=420, y=130, width=300, height=635)
score_scroll.place(x=720, y=130, width=20, height=635)

# Optional: sync mouse wheel scrolling
def on_mousewheel(event):
    score_text.yview_scroll(int(-1*(event.delta/120)), "units")
    words_text.yview_scroll(int(-1*(event.delta/120)), "units")
    return "break"

score_text.bind("<MouseWheel>", on_mousewheel)
words_text.bind("<MouseWheel>", on_mousewheel)

# Populate words
words_text.config(state="normal")
words = [
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "ugli", "vanilla", "watermelon", "xigua", "yam",
    "zucchini", "apricot", "blueberry", "cantaloupe", "dragonfruit", "grapefruit",
    "jackfruit", "apple", "car", "pomello"
]

for word in words:
    words_text.insert("end", word + "\n")

words_text.config(state="disabled")

frame1.tkraise()

root.mainloop()