import tkinter as tk

class Frame3(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="lightblue")
        self.grid(row=0, column=0, sticky="nsew")

        # Words Text + Score Text
        self.words_text = tk.Text(self, font=("Courier", 20, "bold"), wrap="none", state="disabled")
        self.score_text = tk.Text(self, font=("Courier", 20, "bold"), wrap="none", state="disabled")

        # Scrollbar that controls both
        self.scrollbar = tk.Scrollbar(self, command=self.sync_scroll)
        self.words_text.config(yscrollcommand=self.scrollbar.set)
        self.score_text.config(yscrollcommand=self.scrollbar.set)

        # Place widgets
        self.words_text.place(x=50, y=130, width=300, height=635)
        self.score_text.place(x=420, y=130, width=300, height=635)
        self.scrollbar.place(x=720, y=130, width=20, height=635)

        # Mousewheel sync
        self.words_text.bind("<MouseWheel>", self.on_mousewheel)
        self.score_text.bind("<MouseWheel>", self.on_mousewheel)

    def sync_scroll(self, *args):
        self.words_text.yview(*args)
        self.score_text.yview(*args)

    def on_mousewheel(self, event):
        self.words_text.yview_scroll(int(-1*(event.delta/120)), "units")
        self.score_text.yview_scroll(int(-1*(event.delta/120)), "units")
        return "break"