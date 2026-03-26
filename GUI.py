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
frame1.grid(row=0, column=0, sticky="nsew")

for i in range(3):
    frame1.grid_rowconfigure(i, weight=1 if i == 1 else 0) 
    frame1.grid_columnconfigure(i, weight=1 if i == 1 else 0)

start_button = tk.Button(frame1, text="START", command=lambda: show_frame(frame2), font=("Courier", 90, "bold"), bg="white", fg="black")
start_button.grid(row=1, column=1, sticky="nsew", padx=420, pady=(120, 120))

title1 = tk.Label(frame1, text="Scrabble\nAssisitant", font=("Courier", 120), bg="lightblue")
title1.grid(row=0, column=1, sticky="nsew", padx=50, pady=(130, 0))



# ----------------- Frame 2 -----------------
frame2 = tk.Frame(root, bg="lightblue")
frame2.grid(row=0, column=0, sticky="nsew")

for i in range(3):
    frame2.grid_rowconfigure(i, weight=1 if i == 1 else 0) 
    frame2.grid_columnconfigure(i, weight=1 if i == 1 else 0)

label2 = tk.Label(frame2, font=("Courier", 60), text="Enter letters:", bg="lightblue")
label2.grid(row=0, column=1, sticky="nsew", padx=(220, 400), pady=(200, 0))

score_label = tk.Label(frame2, font=("Courier", 55), text="Score:", bg="lightblue")
score_label.grid(row=1, column=1, sticky="nsew", padx=(0, 1130), pady=(450, 20))

score_text = tk.Entry(frame2, font=("Courier", 60))
score_text.grid(row=1, column=1, sticky="nsew", padx=(250, 900), pady=(450, 20))

enter_text = tk.Entry(frame2, font=("Courier", 60))
enter_text.grid(row=1, column=1, sticky="nsew", padx=350, pady=(10, 430))

solve_button = tk.Button(frame2, text="Solve", command=lambda: show_frame(frame3), font=("Courier", 30, "bold"))
solve_button.grid(row=1, column=1, sticky="nsew", padx=(500, 500), pady=(110, 360))

wild_button = tk.Button(frame2, text="Add\nWild", command=add_wild, font=("Courier", 30, "bold"))
wild_button.grid(row=1, column=1, sticky="nsew", padx=(1065, 230), pady=(10, 430))

# ----------------- Frame 3 -----------------
frame3 = tk.Frame(root, bg="lightblue")
frame3.grid(row=0, column=0, sticky="nsew")

label3 = tk.Label(frame3, font=("Courier", 60), text="Words:", bg="lightblue")
label3.grid(row=0, column=0, sticky="nsew", padx=(0, 1350), pady=(30, 800))

filter_label = tk.Label(frame3, font=("Courier", 55), text="Filter Category", bg="lightblue")
filter_label.grid(row=0, column=0, sticky="nsew", padx=(820, 300), pady=(30, 800))

Highest_button = tk.Button(frame3, text="Highest Score", font=("Courier", 30, "bold"))
Highest_button.grid(row=0, column=0, sticky="nsew", padx=(820, 300), pady=(130, 700))

Longest_button = tk.Button(frame3, text="Longest Word", font=("Courier", 30, "bold"))
Longest_button.grid(row=0, column=0, sticky="nsew", padx=(820, 300), pady=(230, 600))

Shortest_button = tk.Button(frame3, text="Shortest Word", font=("Courier", 30, "bold"))
Shortest_button.grid(row=0, column=0, sticky="nsew", padx=(820, 300), pady=(330, 500))

Contains_button = tk.Button(frame3, text="Contains letter:", font=("Courier", 30, "bold"))
Contains_button.grid(row=0, column=0, sticky="nsew", padx=(820, 430), pady=(430, 400))

frame1.tkraise()

root.mainloop()