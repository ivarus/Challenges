'''
Created on Mar 8, 2015

@author: Ivan Varus
'''

import sys
from collections import namedtuple
from itertools import islice
from string import whitespace
from operator import mul

Point = namedtuple('Point', ('x', 'y'))
Segment = namedtuple('Segment', ('origin', 'offset'))


def crossProduct(A, B):
    return A.x * B.y - B.x * A.y


def dotProduct(A, B):
    return sum(map(mul, A, B))


def pointSub(A, B):
    return Point(A.x - B.x, A.y - B.y)


def segmentIntersection(A, B):
    x = crossProduct(A.offset, B.offset)
    sub = pointSub(B.origin, A.origin)
    numt = crossProduct(sub, B.offset)
    numu = crossProduct(sub, A.offset)
    if x == 0:
        if numu == 0:
            if (0 <= dotProduct(sub, A.offset) <= dotProduct(A.offset, A.offset) or
                0 <= dotProduct(sub, B.offset) <= dotProduct(B.offset, B.offset)):
                return True
    else:
        t = numt / x
        u = numu / x
        if 0 <= t <= 1 and 0 <= u <= 1:
            return True
    return False


def segmentFromPoints(A, B):
    return Segment(A, pointSub(B, A))


segments = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        t = line.split(':')
        m = map(lambda e: float(e.strip('()[]' + whitespace)), t[1].split(','))
        segments.append(segmentFromPoints(Point._make(islice(m, 2)),
                                          Point._make(islice(m, 2))))
d = dict((i, set()) for i in range(len(segments)))
for i1, s1 in enumerate(segments):
    for j, s2 in enumerate(islice(segments, i1+1, None)):
        if segmentIntersection(s1, s2):
            i2 = j+i1+1
            d[i1].add(i2)
            d[i2].add(i1)
while True:
    cand, conflicts = sorted(d.items(), key=lambda item: len(item[1]), reverse=True)[0]
    if len(conflicts) == 0:
        break
    else:
        d.pop(cand)
        for e in conflicts:
            d[e].discard(cand)
for k in d:
    print(k+1)
