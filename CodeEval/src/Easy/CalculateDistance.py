'''
Created on Feb 12, 2015

@author: Ivan Varus
'''

import sys
from math import sqrt


def nextdigit(s, prev=0):
    found = False
    t = ''
    for i in range(prev, len(s)):
        if not s[i].isdigit() and s[i] != '-':
            if not found:
                continue
            else:
                break
        found = True
        t += s[i]
    return int(t), i


f = open(sys.argv[1], 'r')
for line in f:
    if not line.strip():
        break
    ax, prev = nextdigit(line, 0)
    ay, prev = nextdigit(line, prev)
    bx, prev = nextdigit(line, prev)
    by, prev = nextdigit(line, prev)
    dx, dy = bx - ax, by - ay
    print(int(sqrt(dx*dx + dy*dy)))
f.close()
