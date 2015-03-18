'''
Created on Mar 18, 2015

@author: Ivan Varus
'''

import sys


def sum_of_mines(ls, i, j, m, n):
    s = sum(ls[k*n+l] == '*'
            for l in range(max(0, j-1), min(n, j+2))
            for k in range(max(0, i-1), min(m, i+2)))
    return s


def solve_gen(ls, m, n):
    for i in range(m):
        for j in range(n):
            if ls[i*n + j] == '*':
                yield '*'
            else:
                yield str(sum_of_mines(ls, i, j, m, n))


with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        size_s, sep, ls = test.partition(';')
        print(''.join(solve_gen(ls, *map(int, size_s.split(',')))))
