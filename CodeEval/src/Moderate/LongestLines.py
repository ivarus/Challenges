'''
Created on Feb 25, 2015

@author: Ivan Varus
'''

import sys


test_cases = open(sys.argv[1], 'r')
numLines = 0
lines = []
for test in test_cases:
    pretty = test.rstrip()
    if not pretty:
        continue
    if not numLines:
        numLines = int(pretty)
        continue
    lines.append(pretty)
lines.sort(key=len, reverse=True)
for l in lines[:numLines]:
    print(l)
test_cases.close()
