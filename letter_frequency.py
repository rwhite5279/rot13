#!/usr/bin/env python3
"""
letter_frequency.py
Takes the AliceInWonderland.txt file and does a letter freqency
analysis on it.
"""

__author__ = "Richard White"
__version__ = "2021-06-01"

import operator     # used to sort dictionary by value

def main():
    letters = {}
    infile = open('AliceInWonderland.txt', 'r')
    for line in infile:
        for letter in line.lower():
            if 97 <= ord(letter) and ord(letter) <= 122:
                # print(letter) 
                if letter in letters.keys():
                    letters[letter] += 1
                else:
                    letters[letter] = 1
    # Get total letter count
    letter_count = 0
    for key in letters.keys():
        letter_count += letters[key]
    # Convert frequencies to percentages
    for key in letters.keys():
        letters[key] = letters[key] / letter_count
    # Reveal results
    for key in sorted(letters.keys()):
        print("('" + key + "':" + str(letters[key]) + ")")

if __name__ == "__main__":
    main()
