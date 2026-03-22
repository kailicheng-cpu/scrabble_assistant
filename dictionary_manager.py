'''
Imports and Reads the dictionary text file
Saving the words in a list
Sorting the list in alphabetical order
Then checking and removing any duplicate words
Finally Writing the Words back into the text file
'''


counter = 0

with open('dictionary.txt', 'r') as file:

    # Reads each line of the file and saves each line as a value in a list
    word_dict = [line.strip() for line in file]

    word_dict.sort()

    # Compares the current and next value in the list
    while counter < (len(word_dict) - 1):

        # If Values are the same, the next one gets removed
        if word_dict[counter] == word_dict[counter+1]:
            word_dict.pop(counter+1)

        else:
            counter +=1
    print(word_dict)

# Writes in each value, of the now sorted and checked list, on a line
with open('dictionary.txt', 'w') as file:
    for i in word_dict:
        file.write( i + "\n")