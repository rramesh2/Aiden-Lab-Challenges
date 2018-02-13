-----Read Me for num2wordmap.py----------

Runs on tkinter (for gui) and written for python 2.7.


-----Guide----
Maps any number to a set of interconnected words with the words' mapping being centered on the isogram "subdermatoglyphic", with the index of each letter being a number from 1-17, with 0 being mapped to a hyphen for inclusion purposes. Therefore, every inputted number is simply converted to a letter based on this mapping.

Program enables encoding of numbers and decoding of words, however words are limited to the numbers they originated from so that the program works simply as a number encoder and then a word decoder for words produced from those numbers (although it also has the neat attribute of simply ignoring excess letters so that if "hello" = 12 for example, and p is not in the mapping, then "pppppphpppepppllppooppp" = 12 as well).

Assumes that inputted number sequence will not start with 0s (python considers these octals, and in conversion 0 is removed by python).