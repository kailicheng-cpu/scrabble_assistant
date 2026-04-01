import tkinter as tk

class Frame1(tk.Frame):
    def __init__(self, master, show_frame):
        super().__init__(master, bg="lightblue")
        self.grid(row=0, column=0, sticky="nsew")

        for i in range(3):
            self.grid_rowconfigure(i, weight=1 if i == 1 else 0) 
            self.grid_columnconfigure(i, weight=1 if i == 1 else 0)

        start_button = tk.Button(self, text="START", command=lambda: show_frame("frame2"), font=("Courier", 90, "bold"), bg="white", fg="black")
        start_button.grid(row=1, column=1, sticky="nsew", padx=420, pady=(120, 120))

        title1 = tk.Label(self, text="Scrabble\nAssisitant", font=("Courier", 120), bg="lightblue")
        title1.grid(row=0, column=1, sticky="nsew", padx=50, pady=(130, 0))