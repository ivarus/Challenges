'''
Created on Feb 22, 2015

@author: Ivan Varus
'''

import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    pretty = test.rstrip()
    if len(pretty) <= 55:
        print(pretty)
    else:
        print(pretty[:40].rsplit(' ', 1)[0]+'... <Read More>')
test_cases.close()
