#!/usr/env/python3
# Practice borrowed from udemy course: python bootcamp

# Check whether a string is a pangram or not. Contains all the letters of the alphabet at least once.

import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    # Create a set of the alphabet
    alphaset = set(alphabet)

    # Remove any spaces from input string
    str1 = str1.replace(' ','')
    print("\nRemove any spaces: ",str1)

    # Convert into all lowercase
    str1 = str1.lower()
    print("\nConvert to lowercase: ",str1)

    # Grab all unique letters from the string
    str1 = set(str1)
    print("\nGrab unique letters ",str1)

    # alphabet set == string set from input
    print("\nIs this a pangram, containing all alphabet letters at least once? ")
    return str1 == alphaset

sentence = "The quick brown fox jumps over the lazy dog"
print(ispangram(sentence))
