'''
Created on 3/3/2015 12:44:27 PM

@author: Ivan Varus
'''

import sys
from itertools import count

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    pretty = test.rstrip()
    if not pretty:
        continue
    ss = pretty
    s = int(ss)
    inv = ss[::-1]
    for i in count(1):
        s += int(inv)
        ss = str(s)
        inv = ss[::-1]
        if inv == ss or i == 100:
            print('{} {}'.format(i, ss))
            break
test_cases.close()
