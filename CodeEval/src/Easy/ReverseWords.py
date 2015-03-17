'''
Created on Feb 11, 2015

@author: Ivan Varus
'''

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if len(test) == 0:
        pass
    words = test.split()
    rwords = [words[i] for i in range(len(words)-1, -1, -1)]
    print(' '.join(rwords))
test_cases.close()
