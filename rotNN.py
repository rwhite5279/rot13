#!/usr/bin/env python3
"""
rotNN.py
This program produces a ROT-NN rotation on text by rotating it forwards
or backwards a specified number of letters to encode/decode it.
"""

__author__ = "Richard White"
__version__ = "2021-06-01"

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
        in_string = "this is a demonstration of the Caesar cipher and how easy it is to crack the encryption. will the computer be able to analyze letter frequencies successfully? One of the real challenges of a task like this is the fact that a shorter writing sample may not allow for the frequencies to resolve themselves into the expected percentages. False positives are certainly a possibility!"
        '''
        print("The input string is: \n" + in_string)
        print("... and the rotate_value is", rotate_value)
        '''
        out_string = rotate(in_string, rotate_value)
        # print("After rotating:")
        print(rotate_value, out_string)
        print()
        '''
        print("We can convert it back by rotating n backwards...")
        out_string = rotate(out_string, -rotate_value)
        print("After rotating backwards...")
        print(out_string)
        '''


if __name__ == "__main__":
    main()
