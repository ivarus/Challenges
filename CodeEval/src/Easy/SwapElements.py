'''
Created on Feb 21, 2015

@author: Ivan Varus
'''

import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    numspositions = test.split(':')
    if len(numspositions) != 2:
        continue
    nums = numspositions[0].split()
    positions = numspositions[1].strip().split(', ')
    for pos in positions:
        ij = pos.split('-')
        if len(ij) != 2:
            continue
        i = int(ij[0])
        j = int(ij[1])
        nums[i], nums[j] = nums[j], nums[i]
    print(' '.join(nums))
test_cases.close()
