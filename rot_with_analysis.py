#!/usr/bin/env python3
"""
rot_with_analysis.py
This program produces a series of ROT-NN rotation results on text and 
then uses frequency analysis to determine which rotation is most likely the correct one.
"""

__author__ = "Richard White"
__version__= "2020-06-01"

import math

def get_frequencies(string):
    """Returns a list of tuples, with letters and accompanying 
    frequencies, in alphabetic order.
    """
    letters = {}            # Dictionary to collect letter frequencies
    letterfreqs = []        # Returns final result
    letter_count = 0        # Counts character values (not spaces, etc)
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
            '''Take ASCII value for character and subtract 97 to get
            A = 0, B = 1, C = 2, etc... Add the amount of rotation n,
            take the mod 26 to wrap around if necessary, then add 97
            to get a new ASCII value, and chr to convert back to the
            new letter. Whew!
            '''
            out_string += chr((((ord(letter) - 97) + n) % 26) + 97)
        else:
            out_string += letter    # Non-letter
    return out_string

def calculate_distance(frequencies1, frequencies2):
    """For each list of frequencies for a permutation, calculate the
    square root of the sum of squares for the distances of those 26
    values. We are calculating the "standard deviation" of one set of
    frequencies from the other set of frequencies. The smallest distance
    will be the for the frequencies which most closely match.
    In our context, that will be the plaintext solution with letter
    frequencies that most closely match English frequencies.
    """
    sum_of_squares = 0
    for i in range(len(frequencies2)):  # don't want to go beyond letters
        sum_of_squares += (abs(frequencies1[i][1] - frequencies2[i][1]))**2
    return math.sqrt(sum_of_squares)

def initialize_english_frequencies():
    """Initializes a set of frequencies for English letters based on
    an analysis of the text of Alice in Wonderland. Each entry in 
    the frequencies list is a tuple with the first value the character,
    and the second value the relative frequency of occurence.
    """
    frequencies = \
    [('a',0.08163018952021023),('b',0.013696340523525205),
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
    return frequencies 
 
def main():
    frequencies = initialize_english_frequencies() 
    print("Identifying likely decryptions with a 26-space vector")
    in_string = "sghr hr z cdlnmrsqzshnm ne sgd bzdrzq bhogdq zmc gnv dzrx hs hr sn bqzbj sgd dmbqxoshnm. vhkk sgd bnlotsdq ad zakd sn zmzkxyd kdssdq eqdptdmbhdr rtbbdrretkkx? nmd ne sgd qdzk bgzkkdmfdr ne z szrj khjd sghr hr sgd ezbs sgzs z rgnqsdq vqhshmf rzlokd lzx mns zkknv enq sgd eqdptdmbhdr sn qdrnkud sgdlrdkudr hmsn sgd dwodbsdc odqbdmszfdr. ezkrd onrhshudr zqd bdqszhmkx z onrrhahkhsx!"
    print("Attempting to decrypt this passage:")
    print(in_string)
    # We'll be looking for a minimum distance between possible decryptions,
    # so start with 1 and key off smaller distances as we go.
    minimum_percentage = 1
    for rotate_value in range(26):
        out_string = rotate(in_string, rotate_value) 
        rot_frequencies = get_frequencies(out_string)
        # This function call below gets the 26-space vector difference 
        # between the frequencies in our test data and the frequencies 
        # in our sample data.
        dist = calculate_distance(frequencies, rot_frequencies)
        print("Translation:", out_string)
        print("Distance:", dist)
        if dist < minimum_percentage:
            minimum_percentage = dist 
            print("Best decryption so far!")
    print("Finished")

if __name__ == "__main__":
    main()
