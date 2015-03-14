'''
Created on Feb 20, 2015

@author: Ivan Varus
'''

import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    words = test.split()
    if len(words) == 0:
        continue
    print(' '.join(map(lambda w: w[0].upper() + w[1:], words)))
test_cases.close()
