'''
Created on Feb 20, 2015

@author: Ivan Varus
'''

import sys
from collections import Counter


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums = test.split()
    if len(nums) == 0:
        continue
    C = Counter(nums)
    try:
        lowest = min(filter(lambda e: e[1] == 1, C.items()))
    except ValueError:
        print(0)
    else:
        print(nums.index(lowest[0])+1)
test_cases.close()
