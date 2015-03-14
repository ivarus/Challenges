'''
Created on Feb 22, 2015

@author: Ivan Varus
'''

import sys


monthtable = {'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3,
              'May': 4, 'Jun': 5, 'Jul': 6, 'Aug': 7,
              'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11}


def isIntersected(A, B):
    if A[1] < B[0] and A[1] < B[1]:
        return False
    if A[0] > B[0] and A[0] > B[1]:
        return False
    return True


def union(A, B):
    return (min(A[0], B[0]), max(A[1], B[1]))


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    alldates = test.split(';')
    allmonths = []
    for x in alldates:
        datepair = x.split('-')
        if len(datepair) != 2:
            continue
        date0 = datepair[0].split()
        date1 = datepair[1].split()
        convertToMonths = lambda my: int(my[1])*12 + monthtable[my[0]]
        months0 = convertToMonths(date0)
        months1 = convertToMonths(date1) + 1  # to the last day of the month
        allmonths.append((months0, months1))
    recheck = True
    while recheck:
        recheck = False
        for i, mi in enumerate(allmonths):
            for j, mj in enumerate(allmonths[i+1:]):
                if isIntersected(mi, mj):
                    allmonths[i] = union(mi, mj)
                    allmonths.pop(j+i+1)
                    recheck = True
                    break
            if recheck:
                break
    exp = sum(map(lambda x: x[1]-x[0], allmonths)) // 12
    print(exp)
test_cases.close()
