'''
Created on Feb 12, 2015

@author: Ivan Varus

Insertion sort
'''

import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    t = test.strip()
    if len(t) == 0:
        pass
    nums = [float(i) for i in t.split()]
    for i in range(1, len(nums)):
        j = i
        while j > 0 and nums[j-1] > nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
    for i in range(0, len(nums)):
        print('{:.3f}'.format(nums[i]), end=' ' if i < len(nums)-1 else '\n')
test_cases.close()
