'''
Created on Feb 28, 2015

@author: Ivan Varus
'''

import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    elems = test.split()
    index = int(elems.pop()) - 1
    if index < len(elems):
        print(elems[len(elems)-1-index])
test_cases.close()
