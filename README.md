README.markdown
===============

PROJECT TITLE: 
Caesar Cipher cryptanalysis

AUTHORS:
Richard White

PURPOSE OF PROJECT:
The files in this package can be used to perform English-language
Caesar Cipher encryptions and automated decryptions based on letter
frequency analysis.

VERSION: 
2017-05-09

FILES INCLUDED:
* AliceInWonderland.txt
* README.markdown (this file)
* letter_frequency.py
* rot13.py
* rotNN.py
* rot_with_analysis.py


HOW TO USE THIS PROJECT:
Take a plaintext phrase or paragraph and encrypt it using the Python file
rotNN.py. (Run the Python3 file from the command line by entering:

    $ python3 rotNN.py

A series of 26 different Caesar rotations will be produced. Select one to be  your Caesar-encrypted string.

To demonstrate the decryption process, place this string into the 
rot_with_analysis.py file. Run this file from the command line using:

    $ python3 rot_with_analysis.py

The program will create a series of rotations using the same process that
was used for encrypting the expression. Additionally, it will perform a
26-space vector analysis of the letter frequencies in those rotations,
attempting to find a solution that has the minimum distance between the
letter frequency for standard English and this particular file. The final
minimum distance will be displayed as the most likely candidate.


FURTHER INFORMATION:
A "Caesar Cipher" is a cipher based on a rotation of the alphabet, and a
ROT-13 cipher is based on a rotation of 13 spaces. Thus:

    Plaintext: a b c d e f g h i j k l m n o p q r s t u v w x y z
    ROT-13   : n o p q r s t u v w x y z a b c d e f g h i j k l m

ROT-13 is perhaps the easiest rotation to work with, because rotation
can be performed either "forwards" or "backwards" through the 26-character
English alphabet with the same result. Instead of always rotating 13
spaces, however, it is possible to rotate an arbitrary number of spaces,
and this is what the ROTNN.py file allows for.

The English language letter frequencies used in this project may be a
bit off from the standard frequencies. The ones in this project were 
created using the complete text of *Alice in Wonderland* (included here
as a text file) and the program letter_frequency.py, included here as
a reference.


