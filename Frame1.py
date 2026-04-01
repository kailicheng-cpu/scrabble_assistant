import tkinter as tk

def create_frame1(root, show_frame_func, frame2):
    frame1 = tk.Frame(root, bg="lightblue")
    frame1.place(x=0, y=0, width=1400, height=800)

    title1 = tk.Label(frame1, text="Scrabble\nAssistant", font=("Courier", 120), bg="lightblue")
    title1.place(x=380, y=130)

    start_button = tk.Button(frame1, text="START", command=lambda: show_frame_func(frame2),
                             font=("Courier", 90, "bold"), bg="white", fg="black")
    start_button.place(x=420, y=430, width=560, height=200)

    return frame1