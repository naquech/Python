"""
Quiz Game: the system will choose a random word from a list of words
and definitions in a file. It will then show the user the random word
and a list of definitions, only one definition matches the word.
If the user doesn't choose the correct definition it will display a
different word.

SAWDUST
---------------
1 tiny bits of wood
2 being uncontrollably violent
3 coming back to consciousness
4 proof to the contrary
Please enter 1, 2, 3, 4 or 0 to exit:

"""

import random


"""
Separates the word from the definition
params: raw string from a file
return: split string into word, definition
"""


def word_definition(rawString):
    word, definition = rawString.split(',', 1)         # (1) Split on the first comma
    return word, definition


"""
Generate a list of random words and associate them
with their definition
Params: list of words, dictionary
Return: word and its definition
"""


def get_definition(w_list, w_dic):
    random_index = random.randrange(len(w_list))
    word = w_list.pop(random_index)                 # Pop the word so it's not repeated
    definition = w_dic.get(word)                    # Acces the definition by the value (word)
    return word, definition


# MAIN

# Read and print file
file_in = open('Vocabulary_list.csv', 'r')
words_list = file_in.readlines()
#print(words_list)

# Remove header from file (word, definition)
words_list.pop(0)

# Remove possible duplicates by using tuples
words_set = set(words_list)

# Write clean set into a new file
file_out = open('Vocabulary_set.csv', 'w')
file_out.writelines(sorted(words_set))

# Create the dictionary
words_dict = dict()

for line in words_set:
    word, definition = word_definition(line)
    words_dict[word] = definition               # word->key, definition->value
    #print(word)

while True:
    words_list = list(words_dict)
    choice_list = []
    for x in range(4):
        word, definition = get_definition(words_list, words_dict)
        choice_list.append(definition)
    random.shuffle(choice_list)                  #shuffle the choices

    print('\n', word.upper())
    print('---------------')

    # print choices
    for idx, choice in enumerate(choice_list):
        print(idx+1, choice)

    choice = int(input('Please enter 1, 2, 3, 4 or 0 to exit: '))

    if choice_list[choice - 1] == definition:
        print('Correct!\n')
    elif choice == 0:
        exit()
    else:
        print('Incorrect')

