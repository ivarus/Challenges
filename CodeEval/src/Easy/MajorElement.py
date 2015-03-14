'''
Created on Feb 21, 2015

@author: Ivan Varus
'''

import sys
from collections import Counter


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    seq = test.split(',')
    seq[-1] = seq[-1].rstrip()
    C = Counter(seq)
    major = C.most_common(1)
    if major and major[0][1] > len(seq) / 2:
        print(major[0][0])
    else:
        print('None')
test_cases.close()
