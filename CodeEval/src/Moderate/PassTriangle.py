'''
Created on Feb 28, 2015

@author: Ivan Varus
'''

import sys


test_cases = open(sys.argv[1], 'r')
rows = []
for test in test_cases:
    rows.append(list(map(int, test.split())))
for level in range(len(rows)-1, 0, -1):
    for col in range(len(rows[level])-1, 0, -1):
        rows[level-1][col-1] += max(rows[level][col], rows[level][col-1])
print(rows[0][0])
test_cases.close()
