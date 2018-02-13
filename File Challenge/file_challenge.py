"""
file_challenge.py

Santiago Garcia Acosta
01/28/2018
Aiden Lab Challenge 2
"""

import os
FOLDER = os.path.dirname(os.path.abspath(__file__))

def filechallenge(file1, file2):
    """
    Reads two different files and creates a new one based on matching beginnings
    of lines on each file.

    Parameters: file1, file2, text files with contents we want to analyze.

    Output: new_file, file created from looking through file1 and file2.
    """

    string1 = open(os.path.join(FOLDER, file1), 'r').read()
    string2 = open(os.path.join(FOLDER, file2), 'r').read()
    new_file = open(os.path.join(FOLDER, 'file3.txt'), 'w')
    string1 += '\n'
    string2 += '\n'
    strings = [string1, string2]

    maps = [{}, {}]

    for charidx in range(2):
        string = strings[charidx]
        idx = 0
        idx_base = 0
        id_found = 0
        for char in string:
            if char == ' ' and not id_found:
                id_val = string[idx_base:idx]
                id_loc = idx
                id_found = 1

            elif char == '\n' and id_found:
                maps[charidx][id_val] = string[id_loc + 1: idx]
                id_found = 0
                idx_base = idx + 1

            idx += 1

    newstr = ""
    for delim in maps[0]:
        if delim in maps[1]:
            newstr += delim + " " + maps[0][delim] + " " + maps[1][delim] + "\n"
    
    new_file.write(newstr)

    return

filechallenge('testfile1.txt', 'testfile2.txt') # input files here
