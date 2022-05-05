#!/usr/env/python3
import random

# The Daily Brew puzzle: in the following code, each symbol stands for one of five letters
# ; stands for N O L U T
# ( stands for K B M E Y
# 3 stands for H E P C W
# * stands for F A J E R


# the Four letter code word  3;*(  can be translated into two english words that are opposites. What are the two words?

three = ['H', 'E', 'P', 'C', 'W']
semicolon = ['N', 'O', 'L', 'U', 'T']
asterisk = ['F', 'A', 'J', 'E', 'R']
parens = ['K', 'B', 'M', 'E', 'Y']


mystery_word = (three + semicolon + asterisk + parens)

#print (three[4] + semicolon[3] + asterisk[2] + parens[1])
#print (three[2] + semicolon[3] + asterisk[4] + parens[1])
#print (three[3] + semicolon[4] + asterisk[1] + parens[2])

# Try using random in range

for num in range(0,5):
    for letter in ('three', 'semicolon', 'asterisk', 'parens'):
        randnum1 = random.randint(0,4)
        randnum2 = random.randint(0,4)
        randnum3 = random.randint(0,4)
        randnum4 = random.randint(0,4)
        new_word = (letter[randnum1] + letter[randnum2] + letter[randnum3] + letter[randnum4])
        print(new_word)


#Word in range {0} HNFK
#Word in range {1} EOAB
#Word in range {2} PLJM
#Word in range {3} CUEE
#Word in range {4} WTRY

# How to match word patterns found with a dictionary of known words?
