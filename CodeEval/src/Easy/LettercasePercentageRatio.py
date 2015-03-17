'''
Created on Feb 12, 2015

@author: Ivan Varus
'''

import sys
test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    l = len(test.strip())
    if l == 0:
        pass
    nupper, nlower = 0, 0
    for c in test:
        if c.isalpha():
            if c.isupper():
                nupper += 1
            else:
                nlower += 1
    print('lowercase: {:.2f} uppercase: {:.2f}'.format(100.0 * nlower/l,
                                                       100.0 * nupper/l))
test_cases.close()
