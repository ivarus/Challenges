'''
Created on Feb 22, 2015

@author: Ivan Varus
'''

import sys


lastcheckpoint = -1

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    pretty = test.rstrip()
    if not pretty:
        continue
    for i, c in enumerate(pretty):
        if c == 'C':
            checkpoint = i
            break
        elif c == '_':
            checkpoint = i
    if lastcheckpoint == checkpoint or lastcheckpoint == -1:
        passway = '|'
    elif lastcheckpoint > checkpoint:
        passway = '/'
    else:
        passway = '\\'
    print(pretty[:checkpoint] + passway + pretty[checkpoint+1:])
    lastcheckpoint = checkpoint
test_cases.close()
