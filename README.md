# Scrabble Game Assistant

A Python-based tool that generates all possible letter combinations from a set of tiles and verifies them against a dictionary to find playable Scrabble words. The program uses a graphical user interface (GUI) for easy interaction and efficient gameplay assistance.

### How It Works:
- The user inputs a set of letters (tiles) into the GUI.
- The ComboFinder class generates all possible combinations.
- The WordVerifications class checks each combination against a NWL (NASPA Word List) sorted dictionary.
- Valid words are displayed in the GUI, ready for gameplay.
- Filters can be applied to refine results (e.g., word length)

## Getting Started

### Dependencies:
- Python 3
- Tkinter (built-in Python GUI library)
- No external libraries required (all standard Python modules)

### Installation:

#### Install Python 3 (if not already installed)
- Download from https://www.python.org/downloads/
- Ensure you add Python to your system PATH during installation.

#### Download Project
- Clone the repository using Git:
```
git clone https://github.com/kailicheng-cpu/scrabble_assistant.git
```
#### Set Up Project Folder
- Navigate to the project folder:

```
cd scrabble_assistant
```

** Ensure Dependencies are installed

### Program Execution:

Run the main file:
```angular2html
python main.py
```
Example:
```
Input: ['C', 'A', 'T']
Output: ['ACT', 'AT', 'CAT']
```
#### Usage Instructions:

- After Start Button pressed, Enter your available letter or wildcard tiles into the input field
- Click the Solve button
- The program displays all valid Scrabble words based on the entered letters
- Filters can be applied to refine the word selection

## Testing:

#### The program includes tests for:
- Valid and invalid word detection
- Edge cases, such as empty input or single letters
- Performance with large datasets
- Runtime is measured to ensure efficiency

## Future Improvements:

- Optimize combination generation further for more efficient and faster runtime

## Contributers:

Finlay Spratt  
Kaili Cheng
