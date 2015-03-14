'''
Created on Mar 1, 2015

@author: Ivan Varus
'''

import sys


def reverseGroups(seq, k):
    offset = k - 1
    while offset < len(seq):
        for i in range(k):
            yield seq[offset-i]
        offset += k
    for i in range(offset-k+1, len(seq)):
        yield seq[i]


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    seq = test.split(',')
    if len(seq) == 0:
        continue
    i = seq[-1].index(';')
    k = int(seq[-1][i+1:])
    seq[-1] = seq[-1][:i]
    print(','.join(reverseGroups(seq, k)))
test_cases.close()
