import tkinter as tk

def create_frame1(root, show_frame_func, frame2):
    """
    Creates the first frame (home/start screen) of the Scrabble Assistant GUI.

    Parameters:

    root : tk.Tk
        The main Tkinter window.
    show_frame_func : function
        A function used to raise/switch to another frame (like show_frame).
    frame2 : tk.Frame
        The next frame to show when the "START" button is pressed.

    Returns:

    frame1 : tk.Frame
        The fully created start screen frame.
    
    Description:

    - Sets up a frame with a light blue background.
    - Displays the title "Scrabble Assistant" in a large font.
    - Adds a "START" button that, when clicked, switches to frame2.
    """
    frame1 = tk.Frame(root, bg="lightblue")
    frame1.place(x=0, y=0, width=1400, height=800)

    # Title label
    title1 = tk.Label(frame1, text="Scrabble\nAssistant", font=("Courier", 120), bg="lightblue")
    title1.place(x=380, y=130)

    # Start button
    start_button = tk.Button(
        frame1, 
        text="START", 
        command=lambda: show_frame_func(frame2),  # Switch to frame2 on click
        font=("Courier", 90, "bold"), 
        bg="white", 
        fg="black"
    )
    start_button.place(x=420, y=430, width=560, height=200)

    return frame1