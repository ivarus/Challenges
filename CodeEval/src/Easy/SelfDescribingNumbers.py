'''
Created on Feb 20, 2015

@author: Ivan Varus
'''

import sys
from collections import Counter


def isSelfDescribing(s):
    C = Counter(s)
    for i, c in enumerate(s):
        if int(c) != C.get(str(i), 0):
            return False
    return True


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if not test:
        continue
    if isSelfDescribing(test):
        print('1')
    else:
        print('0')
test_cases.close()
