'''
Created on Feb 21, 2015

@author: Ivan Varus
'''

import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    digitscodes = test.split()
    if len(digitscodes) != 2:
        continue
    A = []
    B = []
    operation = ''
    for code in digitscodes[1]:
        if code.isalpha():
            i = ord(code) - ord('a')
            if operation:
                B.append(digitscodes[0][i])
            else:
                A.append(digitscodes[0][i])
        else:
            operation = code
    a = int(''.join(A))
    b = int(''.join(B))
    if operation == '+':
        print(a+b)
    else:
        print(a-b)
test_cases.close()
