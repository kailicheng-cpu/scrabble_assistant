import tkinter as tk

def add_wild():
    enter_text.insert(tk.END, "*")

class Frame2(tk.Frame):
    def __init__(self, master, show_frame):
        super().__init__(master, bg="lightblue")
        self.grid(row=0, column=0, sticky="nsew")

        for i in range(3):
            self.grid_rowconfigure(i, weight=1 if i == 1 else 0) 
            self.grid_columnconfigure(i, weight=1 if i == 1 else 0)

        label2 = tk.Label(self, font=("Courier", 60), text="Enter letters:", bg="lightblue")
        label2.grid(row=0, column=1, sticky="nsew", padx=(220, 400), pady=(200, 0))

        score_label = tk.Label(self, font=("Courier", 55), text="Score:", bg="lightblue")
        score_label.grid(row=1, column=1, sticky="nsew", padx=(0, 1130), pady=(450, 20))

        score_text = tk.Entry(self, font=("Courier", 60))
        score_text.grid(row=1, column=1, sticky="nsew", padx=(250, 900), pady=(450, 20))

        enter_text = tk.Entry(self, font=("Courier", 60))
        enter_text.grid(row=1, column=1, sticky="nsew", padx=350, pady=(10, 430))

        solve_button = tk.Button(self, text="Solve", command=lambda: show_frame(frame3), font=("Courier", 30, "bold"))
        solve_button.grid(row=1, column=1, sticky="nsew", padx=(500, 500), pady=(110, 360))

        wild_button = tk.Button(self, text="Add\nWild", command=add_wild, font=("Courier", 30, "bold"))
        wild_button.grid(row=1, column=1, sticky="nsew", padx=(1065, 230), pady=(10, 430))