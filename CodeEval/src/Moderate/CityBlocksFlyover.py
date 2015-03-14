'''
Created on Mar 1, 2015

@author: Ivan Varus
'''

import sys


def flyover(xs, ys):
    ratio = ys[-1] / xs[-1]
    solutions = 0
    for i in range(1, len(xs)):
        for j in range(1, len(ys)):
            if xs[i-1] * ratio < ys[j] and xs[i] * ratio > ys[j-1]:
                solutions += 1
    return solutions

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    args = []
    for t in test.split():
        args.append(list(map(int, t.strip('()').split(','))))
    if args:
        print(flyover(*args))
test_cases.close()
