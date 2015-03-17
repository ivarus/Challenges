'''
Created on Mar 5, 2015

@author: Ivan Varus

@thanks: ferhatelmas/algo
'''

import sys


def predict(n):
    return bin(n).count('1') % 3


f = open(sys.argv[1], 'r')
for line in f:
    print(predict(int(line)))
f.close()
