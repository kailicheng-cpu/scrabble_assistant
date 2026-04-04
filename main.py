import tkinter as tk
from utils import show_frame
from Frame1 import create_frame1
from Frame2 import create_frame2
from Frame3 import create_frame3
from Frame4 import create_frame4

root = tk.Tk()  # Main window
root.geometry("1400x800")  # Set window size

# Create frames and get important widgets
frame4, enter_word, back_button = create_frame4(root, show_frame, None)
frame3, letterN_filter, letter_filter, words_text, score_list, next_button = create_frame3(root, frame2=None)
frame2, enter_text, score_text = create_frame2(root, show_frame, frame3, frame4, words_text, score_list)
frame1 = create_frame1(root, show_frame, frame2)

# Set button commands for navigation
next_button.config(command=lambda: show_frame(frame2))
back_button.config(command=lambda: show_frame(frame2))
frame1.children['!button'].config(command=lambda: show_frame(frame2))

frame1.tkraise()  # Show the main menu first
root.mainloop()   # Start GUI