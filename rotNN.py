#!/usr/bin/env python3
"""
rotNN.py
This program produces a ROT-NN rotation on text by rotating it forwards
or backwards a specified number of letters to encode/decode it.
@author Richard White
@version 2017-05-09
"""

def rotate(in_string, n):
    """Takes an input string and rotates it n letters in the English
    alphabet. 
    """
    out_string = ""
    for letter in in_string.lower():
        if 97 <= ord(letter) and ord(letter) <= 122: # lowercase letters
            out_string += chr((((ord(letter) - 97) + n) % 26) + 97)
        else:
            out_string += letter    # Non-letter
    return out_string

def main():
    print("ROT-NN Demonstration")
    for rotate_value in range(26):
        # in_string = "Now is the time for all good men (and women) to come to the aid of their country".lower()
        in_string = "Today is Craig Fletcher's birthday"
        '''
        print("The input string is: \n" + in_string)
        print("... and the rotate_value is", rotate_value)
        '''
        out_string = rotate(in_string, rotate_value)
        # print("After rotating:")
        print(rotate_value, out_string)
        '''
        print("We can convert it back by rotating n backwards...")
        out_string = rotate(out_string, -rotate_value)
        print("After rotating backwards...")
        print(out_string)
        '''


if __name__ == "__main__":
    main()
