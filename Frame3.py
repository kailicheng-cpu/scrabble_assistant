import tkinter as tk
from utils import validate_single_alpha, validate_single_digit, show_frame, update_highest_score, update_longest_word, update_shortest_word, update_contains_letter, update_word_length
from WordFilter import WordFilter
from Frame2 import generator

def create_frame3(root, frame2):
    """
    Creates frame3, the results and word-filtering interface for the Scrabble Assistant.

    Parameters:

    root : tk.Tk
        The main Tkinter window.
    frame2 : tk.Frame
        The previous frame where letters are entered, used for returning via "Next Round"

    Returns:

        - frame3: the Tkinter frame containing all results and filters.
        - letterN_filter: Entry widget for specifying word length filter.
        - letter_filter: Entry widget for specifying letter-contained filter.
        - words_text: Text widget displaying filtered/generated words.
        - score_list: Text widget displaying corresponding scores.
        - next_button: Button widget to go back to frame2.

    Description:

    - Initializes frame3 with a light blue background.
    - Creates a WordFilter object linked to the global generator to handle scoring and filtering.
    - Sets up labels for "Words", "Score", and "Filter Category".
    - Adds filter buttons:
        * "Highest Score" shows highest scoring words.
        * "Longest Word" shows the longest words.
        * "Shortest Word" shows the shortest words.
        * "Number of letters" filters by word length using the letterN_filter Entry.
        * "Contains letter" filters words containing a specific letter from letter_filter Entry.
    - Adds Entry widgets with validation:
        * letterN_filter accepts only single digits.
        * letter_filter accepts only single alphabetic letters.
    - Includes a "Next Round" button to return to frame2.
    - Sets up words_text and score_list Text widgets with a shared vertical scrollbar.
    - Synchronizes mouse wheel scrolling between words_text and score_list
    """
    # Setup background
    frame3 = tk.Frame(root, bg="lightblue")
    frame3.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Initialize word filter object
    word_filter = WordFilter(generator)

    frame3.valid_words = []

    # Labels
    words_label = tk.Label(frame3, font=("Courier", 50), text="Words", bg="lightblue")
    words_label.place(x=50, y=30)

    score_label = tk.Label(frame3, text="Score", font=("Courier", 50), bg="lightblue")
    score_label.place(x=370, y=12, width=300, height=100)

    filter_label = tk.Label(frame3, font=("Courier", 55), text="Filter Category", bg="lightblue")
    filter_label.place(x=820, y=30)

    # Filter Buttons
    Highest_button = tk.Button(frame3, text="Highest Score", font=("Courier", 30, "bold"), command=lambda: update_highest_score(word_filter, words_text, score_list))
    Highest_button.place(x=820, y=130, width=500, height=70)

    Longest_button = tk.Button(frame3, text="Longest Word", command=lambda: update_longest_word(word_filter, words_text, score_list), font=("Courier", 30, "bold"))
    Longest_button.place(x=820, y=230, width=500, height=70)

    Shortest_button = tk.Button(frame3, text="Shortest Word", command=lambda: update_shortest_word(word_filter, words_text, score_list), font=("Courier", 30, "bold"))
    Shortest_button.place(x=820, y=330, width=500, height=70)

    letters_button = tk.Button(frame3, text="Number of letters:", command=lambda: update_word_length(word_filter, words_text, score_list, letterN_filter.get()), font=("Courier", 30, "bold"))
    letters_button.place(x=820, y=430, width=380, height=70)

    Contains_button = tk.Button(frame3, text="Contains letter:", command=lambda: update_contains_letter(word_filter, words_text, score_list, letter_filter.get()), font=("Courier", 30, "bold"))
    Contains_button.place(x=820, y=530, width=380, height=70)

    # Text entries for filters 
    vcmd_digit = (root.register(validate_single_digit), '%P')
    letterN_filter = tk.Entry(frame3, font=("Courier", 50), validate="key", validatecommand=vcmd_digit)
    letterN_filter.place(x=1210, y=430, width=110, height=70)

    vcmd_alpha = (root.register(validate_single_alpha), '%P')
    letter_filter = tk.Entry(frame3, font=("Courier", 50), validate="key", validatecommand=vcmd_alpha)
    letter_filter.place(x=1210, y=530, width=110, height=70)

    # Button to return to frame 2
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

# -------------------- Testing ----------------------

"""
Manual testing

Test 1: Highest score button

Action: Click "Highest Score"
Expected: Only highest scoring words displayed
Actual: Only top scoring words shown
Result: PASS

Test 2: Longest word button

Action: Click "Longest Word"
Expected: Only longest words displayed
Actual: Longest words shown correctly
Result: PASS

Test 3: Shortest word button

Action: Click "Shortest Word"
Expected: Only shortest words displayed
Actual: Shortest words shown correctly
Result: PASS

Test 4: Valid length input (Number of letters)

Input: 3
Action: Click "Number of letters"
Expected: Only 3-letter words displayed
Actual: Correct words shown
Result: PASS

Test 5: Invalid input (letter instead of number)

Input: "A"
Expected: Input rejected (only digits allowed)
Actual: Letter not entered
Result: PASS

Test 6: Empty input for Number of letters

Input: ""
Action: Click button
Expected: No change
Actual: Error message in terminal but did not affect anything on screen
Result: PASS

Test 7: Valid letter filter

Input: "A"
Action: Click "Contains letter"
Expected: Only words containing "A"
Actual: Filter worked correctly
Result: PASS

Test 8: Lowercase letter input

Input: "a"
Expected: Treated same as uppercase
Actual: Works correctly
Result: PASS

Test 9: Invalid input (number)

Input: "1"
Expected: Input rejected
Actual: Number not entered
Result: PASS

Test 10: Scrollbar sync

Action: Scroll using scrollbar
Expected: Words and scores scroll together
Actual: Both boxes scroll in sync
Result: PASS

Test 11: Mouse wheel scroll

Action: Use mouse wheel
Expected: Both text boxes scroll together
Actual: Scrolling synced correctly
Result: PASS

Test 12: Return to frame2

Action: Click "Next Round"
Expected: Return to input screen (frame2)
Actual: Frame changed correctly
Result: PASS

Test 13: Multiple filters in a row

Action: Click multiple filter buttons (e.g., Highest → Longest → Shortest)
Expected: Each filter updates results correctly
Actual: Filters applied correctly each time
Result: PASS

Test 14: No matching results

Input: Letter or length with no matches
Expected: Empty result displayed
Actual: No words shown
Result: PASS

"""