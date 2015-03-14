'''
Created on Feb 21, 2015

@author: Ivan Varus
'''

import sys


table = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400),
         ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
         ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if not test:
        continue
    num = int(test)
    rom = []
    for r, n in table:
        while num - n >= 0:
            num -= n
            rom.append(r)
    print(''.join(rom))
test_cases.close()
