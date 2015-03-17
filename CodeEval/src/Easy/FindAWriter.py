'''
Created on Feb 12, 2015

@author: Ivan Varus
'''

import sys

f = open(sys.argv[1], 'r')
for line in f:
    letternums = line.split('|')
    if len(letternums) != 2:
        pass
    for c in letternums[1].split():
        n = int(c)
        print(letternums[0][n-1], end='')
    print('')
f.close()
