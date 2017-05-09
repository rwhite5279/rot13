#!/usr/bin/env python3
"""
letter_frequency.py
Takes the AliceInWonderland.txt file and does a letter freqency
analysis on it.
"""

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

    frequencies = sorted(letters.items(), key=operator.itemgetter(1))
    frequencies.reverse()
    for frequency in frequencies:
        print(frequency[0])






if __name__ == "__main__":
    main()
