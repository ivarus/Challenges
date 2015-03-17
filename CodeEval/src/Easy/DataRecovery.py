'''
Created on Feb 11, 2015

@author: Ivan Varus
'''


import sys

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    wordsnums = test.split(';')
    if (len(wordsnums) == 2):
        words = wordsnums[0].split(' ')
        nums = [int(c) for c in wordsnums[1].split(' ')]
        miss = []
        for i in range(1, len(words)+1):
            if i not in nums:
                miss.append(i)
        D = {}
        for i in range(0, len(words)):
            if i < len(nums):
                D[nums[i]] = words[i]
            else:
                D[miss[len(nums)-i]] = words[i]
        print(' '.join(D.values()))
test_cases.close()
