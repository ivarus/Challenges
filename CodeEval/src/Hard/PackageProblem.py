'''
Created on Mar 7, 2015

@author: Ivan Varus

Improved version of https://github.com/ferhatelmas/
'''

import sys


def pack(maxWeight, things):
    things = map(lambda e: (int(e[0]), float(e[1]), int(e[2][1:])), things)
    d = {tuple(): (0, 0)}
    for t in things:
        nd = {}
        for k, v in d.items():
            if v[1] + t[1] <= maxWeight:
                nd[k + (t[0],)] = (v[0] + t[2], v[1] + t[1])
            nd[k] = v
        d = nd
    k = sorted(d.items(), key=lambda e: (-e[1][0], e[1][1]))[0][0]
    return ','.join(map(str, k)) if k else '-'


with open(sys.argv[1], 'r') as f:
    for line in f:
        t = line.split(':')
        print(pack(int(t[0]), map(lambda e: e.strip('()').split(','), t[1].split())))
