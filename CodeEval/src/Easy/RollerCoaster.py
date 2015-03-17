'''
Created on Feb 11, 2015

@author: Ivan Varus
'''

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    flag = True
    out = ''
    for i in range(0, len(test)):
        if test[i].isalpha():
            c = test[i].upper() if flag else test[i].lower()
            flag = not flag
        else:
            c = test[i]
        out += c
    print(out)
test_cases.close()
