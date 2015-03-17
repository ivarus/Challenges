'''
Created on Mar 4, 2015

@author: Ivan Varus
'''


import sys


def match(patternChar, text):
    if 'B' in text:
        if patternChar == '0' or 'A' in text:
            return False
    return True


def checkSequence(pattern, text, matchMatrix, i=0, j=0):
    if matchMatrix[-1][-1]:
        return
    if i >= len(pattern) or j >= len(text):
        return
    if matchMatrix[i][j]:
        return
    for jj in range(j, len(text)):
        matchMatrix[i][jj] = False
        if match(pattern[i], text[j:jj+1]):
            matchMatrix[i][jj] = True
            checkSequence(pattern, text, matchMatrix, i+1, jj+1)
        else:
            break


f = open(sys.argv[1], 'r')
for line in f:
    pattern, sep, text = line.rstrip().partition(' ')
    if (not pattern) or (not text):
        continue
    matchMatrix = [[None] * len(text) for i in range(len(pattern))]
    checkSequence(pattern, text, matchMatrix)
    if matchMatrix[-1][-1]:
        print('Yes')
    else:
        print('No')
f.close()
