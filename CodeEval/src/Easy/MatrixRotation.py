'''
Created on Feb 18, 2015

@author: Ivan Varus
'''

import sys
import math

f = open(sys.argv[1], 'r')
for line in f:
    M = line.split()
    if len(M) == 0:
        continue
    msize = int(math.sqrt(len(M)))
    rM = []
    for i in range(0, msize):
        for j in range(msize-1, -1, -1):
            rM.append(M[j*msize+i])
    print(' '.join(rM))
f.close()
