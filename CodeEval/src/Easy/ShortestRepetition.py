'''
Created on Feb 21, 2015

@author: Ivan Varus
'''

import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if not test:
        continue
    length = len(test)
    period = length
    for i in range(1, length//2+1):
        if length % i != 0:
            continue
        if test[:i]*(length//i) == test:
            period = i
            break
    print(period)
test_cases.close()
