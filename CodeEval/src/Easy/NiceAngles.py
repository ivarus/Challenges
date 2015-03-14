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
    angle = float(pretty)
    whole = int(angle)
    fract = angle - whole
    minsec = int(3600.0 * fract)
    mins = minsec // 60
    sec = minsec % 60
    print('{}.{:02d}\'{:02d}"'.format(whole, mins, sec))
test_cases.close()
