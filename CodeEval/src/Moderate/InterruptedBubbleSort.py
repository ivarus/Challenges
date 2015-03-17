'''
Created on 3/3/2015 1:36:17 PM

@author: Ivan Varus
'''

import sys
from itertools import islice


def bubble(lst, skip):
    held = lst[0]
    for i, v in enumerate(islice(lst, 1, len(lst)-skip)):
        if v > held:
            v, held = held, v
        lst[i] = v
    lst[-skip-1] = held


def interruptedBubbleSort(lst, max_i):
    for skip in range(min(max_i, len(lst))):
        bubble(lst, skip)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    nums, sep, max_i = test.rpartition('|')
    if len(nums) == 0:
        continue
    max_i = int(nums[-1])
    del nums[-2:]
    nums = list(map(int, nums))
    interruptedBubbleSort(nums, max_i)
    print(' '.join(map(str, nums)))
test_cases.close()
