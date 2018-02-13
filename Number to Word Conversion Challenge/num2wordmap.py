"""
num2wordmap.py

Santiago Garcia Acosta
02/12/2018
Aiden Lab Challenge 1B
"""

import Tkinter
import re

mapp = {0: '-',
        1: 's',
        2: 'u',
        3: 'b',
        4: 'd',
        5: 'e',
        6: 'r',
        7: 'm',
        8: 'a',
        9: 't',
        10: 'o',
        11: 'g',
        12: 'l',
        13: 'y',
        14: 'p',
        15: 'h',
        16: 'i',
        17: 'c'
        }


def conv_num(num, mapp):
    """
    Converts the inputted number following the provided mapping. Assumes maximum two digit
    conversion in mapping. Note that leading zeros will result in incorrect output.

    Parameters: num, the number to be encoded; mapp, the mapping being followed to encode
    the number.

    Output: new_str, the encoded version of the inputted number.
    """

    # Convert number to character array
    str_num = str(num)

    # Encode number
    new_str = ""
    while str_num:
        if str_num[0] == '0':
            new_str += mapp[0]
            if len(str_num) > 1:
                str_num = str_num[1:]

        cur_coup = int(str_num[0:2])

        if cur_coup in mapp:
            new_str = new_str + mapp[cur_coup]
            str_num = str_num[2:]
        else:
            new_str = new_str + mapp[int(str_num[0])]
            str_num = str_num[1:]

    return new_str


def conv_wrd(wrd, mapp):
    """
    Converts the inputted string into an integer following the provided mapping. Assume
    mapping has key as number and value as letter.

    Parameters: wrd, the word to be encoded/decoded; mapp, the mapping being followed
    to convert the word.

    Output: num, the encoded version of the inputted word.
    """

    # Encode word
    num = ""
    vals = mapp.items()
    for letter in wrd:
        for item in vals:
            if item[1] == letter:
                num += str(item[0])

    return int(num)



class num2wordmapping(Tkinter.Tk):
    """
    Simple class for gui implementation through tkinter for code below.
    """

    def __init__(self, parent):
        Tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.initialize()
    
    def initialize(self):
        self.grid()

        self.entryVariable = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable = self.entryVariable)
        self.entry.grid(column = 0, row = 0, sticky = 'EW')
        self.entry.bind("<Return>", self.OnPressEnter)

        button = Tkinter.Button(self, text=u"Convert", command = self.OnButtonClick)
        button.grid(column = 1, row = 0)

        self.labelVariable = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable = self.labelVariable, anchor = 'w', fg = 'black', bg = 'white')
        label.grid(column = 0, row  = 1, columnspan = 2, sticky = 'EW')

        self.grid_columnconfigure(0, weight = 1)

    def OnButtonClick(self):
        found = self.entryVariable.get()
        if bool(re.search('[a-zA-Z]', found)):
            self.labelVariable.set(conv_wrd(found, mapp))
        else:
            self.labelVariable.set(conv_num(int(found), mapp))
        

    def OnPressEnter(self, event):
        found = self.entryVariable.get()
        if bool(re.search('[a-zA-Z]', found)):
            self.labelVariable.set(conv_wrd(found, mapp))
        else:
            self.labelVariable.set(conv_num(int(found), mapp))


# Start GUI
if __name__ == "__main__":
    app = num2wordmapping(None)
    app.title('Number to Word Converter') 
    app.mainloop()
    
