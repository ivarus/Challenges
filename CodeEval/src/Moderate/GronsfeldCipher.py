'''
Created on Mar 7, 2015

@author: Ivan Varus
'''

import sys


VOCAB = ' !"#$%&\'()*+,-./0123456789:<=>?@\
ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
VLEN = len(VOCAB)


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    key, sep, encipher = test.strip().rpartition(';')
    klen = len(key)
    decipher = []
    for i, c in enumerate(encipher):
        pos = VOCAB.index(c)
        shift = int(key[i % klen])
        decipher.append(VOCAB[pos-shift])
    print(''.join(decipher))
test_cases.close()
