'''
Created on Mar 4, 2015

@author: Ivan Varus
'''

import sys
from itertools import islice


def sumOfLife(M, i, j):
    s = sum(M[i+k][j+l] for k in range(-1, 2) for l in range(-1, 2))
    return s


def printField(field):
    for i in range(1, len(field)-1):
        print(''.join(map(lambda x: '*' if x else '.',
                          islice(field[i], 1, len(field[i])-1))))


N = 100 + 2
MAX_I = 10
f = open(sys.argv[1], 'r')
field = [[0]*N]
for line in f:
    field.append([0] + list(map(lambda x: 1 if x == '*' else 0,
                            line.rstrip())) + [0])
f.close()
field.append([0]*N)
buffer = [[0]*N for i in range(N)]
for _ in range(MAX_I):
    for i in range(1, N-1):
        for j in range(1, N-1):
            s = sumOfLife(field, i, j)
            if s == 3:
                buffer[i][j] = 1
            elif s == 4:
                buffer[i][j] = field[i][j]
            else:
                buffer[i][j] = 0
    field, buffer = buffer, field
printField(field)
