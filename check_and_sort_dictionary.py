'''
Imports and Reads the dictionary text file
Saving the words in a list
Sorting the list in alphabetical order
Then checking and removing any duplicate words
Finally Writing the Words back into the text file
'''

# TODO: Make this sort the file properly

counter = 0

with open('dictionary.txt', 'r') as file:
    word_dict = [line.strip() for line in file]

    word_dict.sort()

    while counter < (len(word_dict) - 1):
        if word_dict[counter] == word_dict[counter+1]:
            word_dict.pop(counter+1)

        else:
            counter +=1
    print(word_dict)

with open('dictionary.txt', 'w') as file:
    for i in word_dict:
        file.write( i + "\n")