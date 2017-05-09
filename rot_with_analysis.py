#!/usr/bin/env python3
"""
rot_with_analysis.py
This program produces a series of ROT-NN rotation results on text and 
then uses frequency analysis to determine which rotation is most likely the correct one.
@author Richard White
@version 2017-05-09
"""

import math
import operator

def get_frequencies(string):
    """Returns a dictionary of letters for the string, with accompanying 
    frequencies, in alphabetic order
    """
    letters = {}
    letterfreqs = []
    letter_count = 0
    for letter in string:
        if 97 <= ord(letter) and ord(letter) <= 122:
            letter_count += 1
            if letter in letters.keys():
                letters[letter] += 1
            else:
                letters[letter] = 1 
    # produce percentages and sort
    for key in sorted(letters.keys()):
        letterfreqs.append((key, letters[key] / letter_count))
    return letterfreqs

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

def calculate_distance(frequencies1, frequencies2):
    sum_of_squares = 0
    for i in range(len(frequencies2)):  # don't want to go beyond letters
        # print("Checking",frequencies2[i][0],":")
        # print(abs(frequencies1[i][1] - frequencies2[i][1]))
        sum_of_squares += (abs(frequencies1[i][1] - frequencies2[i][1]))**2
    return math.sqrt(sum_of_squares)

def main():
    frequencies = [('a',0.08163018952021023),('b',0.013696340523525205),
    ('c',0.022266999712144707), ('d',0.04577827713964696),
    ('e',0.12602490412561634),('f',0.018571309184440957),
    ('g',0.02350199177291003),('h',0.06847241696303381),
    ('i',0.06974455164216802), ('j',0.0013557055704641898),
    ('k',0.010752788017791315),('l',0.043763290093135114),
    ('m',0.019537017262031886),('n',0.06512029565524222),
    ('o',0.0756316566536358), ('p',0.01415133759854401),
    ('q',0.00194070180977408),('r',0.05048610401790274), 
    ('s',0.06035675484943311),('t',0.09923579062706026),
    ('u',0.03217479316204396), ('v',0.007855663785018525),
    ('w',0.024848411688782),('x',0.0013742768796486309), 
    ('y',0.021004150687602724),('z',0.0007242810581931973)]
    
    print("Identifying likely decryptions with a 26-space vector")
    # in_string = "a'e kladd zsnafy kgew vaxxaumdlq ywllafy lzak lzafy lg jwugyfarw lzw lwpl zwjw, tml a lzafc al'k bmkl twusmkw a vgf'l zsnw s jwsddq, jwsddq, jwsddq jwhjwkwflslanw ksehdw gx ojalafy. a ewsf, a'e fgl vgafy sfq cafv gx 'imauc tjgof xgp bmehwv gnwj lzw dsrq vgy' cafv gx lzafy zwjw, al'k bmkl kgew ogjvk. "
    in_string = "fapmk ue odmus rxqfotqd'e nudftpmk"
    minimum_percentage = 1.00
    for rotate_value in range(26):
        out_string = rotate(in_string, rotate_value) 
        rot_frequencies = get_frequencies(out_string)
        # This function call below gets the 26-space vector difference 
        # between the frequencies in our test data and the frequencies 
        # in our sample data.
        dist = calculate_distance(frequencies, rot_frequencies)
        if dist < minimum_percentage:
            minimum_percentage = dist 
            print("Checking", out_string)
            print("With a score of",minimum_percentage,"this is the best guess so far.")
            input()

if __name__ == "__main__":
    main()
