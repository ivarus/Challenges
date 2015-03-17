'''
Created on Feb 12, 2015

@author: Ivan Varus
'''

import sys
import collections

test_cases = open(sys.argv[1], 'r')
if not test_cases:
    exit(1)
for test in test_cases:
    t = test.strip()
    if len(t) == 0:
        pass
    t = t.lower()
    counter = collections.Counter(t)
    c = 26
    beauty = 0
    for key, value in counter.most_common():
        if key.isalpha():
            beauty += value*c
            c -= 1
    print(beauty)
test_cases.close()
