'''
Created on Feb 22, 2015

@author: Ivan Varus
'''

import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    pretty = test.rstrip()
    if not pretty:
        continue
    rows = pretty.split(',')
    lowest = len(rows)
    for r in rows:
        xlast, yfirst = 0, len(r)
        for i, c in enumerate(r):
            if c == 'X':
                xlast = i
            if c == 'Y':
                yfirst = i
                break
        d = (yfirst-1) - xlast
        if d < lowest:
            lowest = d
        if lowest == 0:
            break
    print(lowest)
test_cases.close()
