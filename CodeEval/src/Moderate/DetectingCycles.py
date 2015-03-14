'''
Created on Feb 25, 2015

@author: Ivan Varus
'''

import sys


def findCycle(l):
    seen = dict()
    for i, x in enumerate(l):
        if x in seen:
            return l[seen[x]:i]
        seen[x] = i
    return None

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    L = test.split()
    cycle = findCycle(L)
    if cycle:
        print(' '.join(cycle))
test_cases.close()
