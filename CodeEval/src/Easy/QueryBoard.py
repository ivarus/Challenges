'''
Created on Feb 20, 2015

@author: Ivan Varus
'''

import sys
import array as arr


M = [arr.array('B', [0]*256) for i in range(256)]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    cix = test.split()
    if len(cix) < 2:
        continue
    if cix[0] == 'SetCol':
        col = int(cix[1])
        x = int(cix[2])
        for i in range(256):
            M[i][col] = x
    elif cix[0] == 'SetRow':
        row = int(cix[1])
        x = int(cix[2])
        for i in range(256):
            M[row][i] = x
    elif cix[0] == 'QueryRow':
        row = int(cix[1])
        s = sum(M[row])
        print(s)
    elif cix[0] == 'QueryCol':
        col = int(cix[1])
        s = 0
        for i in range(256):
            s += M[i][col]
        print(s)
    else:  # unknown command
        continue
test_cases.close()
