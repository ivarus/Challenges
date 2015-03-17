'''
Created on Feb 12, 2015

@author: Ivan Varus
'''


import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    t = test.strip()
    if len(t) == 0:
        pass
    s = 0
    for c in t:
        if c.isdigit():
            s += (ord(c) - 48)
    print(s)
test_cases.close()
