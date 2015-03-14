'''
Created on Feb 21, 2015

@author: Ivan Varus
'''

import sys


morseTable = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}

morseTableInverse = {v: k for k, v in morseTable.items()}


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    pretty = test.strip()
    if not pretty:
        continue
    morseWords = pretty.split(' ')
    result = []
    for w in morseWords:
        if w == '':
            result.append(' ')
        else:
            result.append(morseTableInverse[w])
    print(''.join(result))
test_cases.close()
