'''
Created on Feb 21, 2015

@author: Ivan Varus
'''

import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    digits = test.split()
    if len(digits) == 0:
        continue
    add = 1
    check = digits[0]
    toprint = []
    for d in digits[1:]:
        if check == d:
            add += 1
        else:
            toprint.append(str(add))
            toprint.append(check)
            check = d
            add = 1
    else:
        toprint.append(str(add))
        toprint.append(check)
    print(' '.join(toprint))
test_cases.close()
