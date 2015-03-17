'''
Created on Feb 18, 2015

@author: Ivan Varus
'''

import sys

f = open(sys.argv[1], 'r')
for line in f:
    s = line.strip()
    l = len(s)
    if l == 0:
        continue
    add = 0
    for c in s:
        add += int(c) ** l
    print(add == int(s))
f.close()
