'''
Created on Feb 20, 2015

@author: Ivan Varus
'''

import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print(test.swapcase())
test_cases.close()
