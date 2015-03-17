'''
Created on Feb 10, 2015

@author: Ivan Varus
'''

import sys

if __name__ == '__main__':

    if len(sys.argv) != 2:
        print('Usage: FizzBuzz sample.txt')
        exit(1)

    f = open(sys.argv[1])
    if not f:
        print('Error opening file')
        exit(1)

    for test in f:
        inums = test.split()
        if len(inums) == 3:
            onums = []
            for i in range(1, int(inums[2]) + 1):
                onum = ''
                if i % int(inums[0]) == 0:
                    onum = 'F'
                if i % int(inums[1]) == 0:
                    onum = onum + 'B'
                if len(onum) == 0:
                    onum = str(i)
                onums.append(onum)
            print(' '.join(onums))
    f.close()
