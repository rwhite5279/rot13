#!/usr/bin/env python3
"""
rot13.py
This program produces a ROT-13 rotation on text to encode/decode it.
"""

__author__ = "Richard White"
__version__ = "2021-06-01"

def rotate(in_string):
    """Takes an input string and rotates it 13 letters in the English
    alphabet. (Note that rotating forwards or backwards doesn't matter,
    because 13 is half of 26.)
    """
    out_string = ""
    for letter in in_string:
        if 65 <= ord(letter) and ord(letter) <= 90: # uppercase letters
            # cool ROT-13 conversion!
            out_string += chr((((ord(letter) - 65) + 13) % 26) + 65)
        else:
            out_string += letter    # Non-letter
    return out_string

def main():
    print("ROT-13 Demonstration")
    in_string = input("Enter message: ")
    print("The input string is: \n" + in_string)
    out_string = rotate(in_string)
    print("After rotating:")
    print(out_string)
    print("We can convert it back by rotating 13 again...")
    out_string = rotate(out_string)
    print("After rotating a second time:")
    print(out_string)


if __name__ == "__main__":
    main()
