import tkinter as tk
from utils import show_frame
from Frame1 import create_frame1
from Frame2 import create_frame2
from Frame3 import create_frame3
from Frame4 import create_frame4

root = tk.Tk()
root.geometry("1400x800")

# Create frames
frame4 = create_frame4(root, show_frame, None)

frame3, letterN_filter, letter_filter, words_text, score_list = create_frame3(root, frame2=None)

# Pass words_text to frame2
frame2, enter_text, score_text = create_frame2(root, show_frame, frame3, frame4, words_text, score_list)

# frame 1
frame1 = create_frame1(root, show_frame, frame2)


# Update frame references after all frames are created
frame1.children['!button'].config(command=lambda: show_frame(frame2))

frame1.tkraise()
root.mainloop()