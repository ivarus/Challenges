'''
Created on Feb 19, 2015

@author: Ivan Varus
'''

import sys
from itertools import product

deltas = list(product((-2, 2), (-1, 1))) + list(product((-1, 1), (-2, 2)))


def knightMoves(position):
    validPos = lambda xy: xy[0] >= 0 and xy[1] >= 0 and xy[0] < 8 and xy[1] < 8
    m = map(lambda xy: (position[0]+xy[0], position[1]+xy[1]), deltas)
    return filter(validPos, m)


f = open(sys.argv[1], 'r')
for line in f:
    s = line.strip()
    if len(s) != 2:
        continue
    position = (ord(s[0])-ord('a'), ord(s[1])-ord('1'))
    moves = knightMoves(position)
    print(' '.join(sorted(map(lambda xy: chr(xy[0]+ord('a')) + chr(xy[1]+ord('1')), moves))))
f.close()
