'''
Created on Feb 18, 2015

@author: Ivan Varus
'''

import sys

digitsmap = '''\
-**----*--***--***---*---****--**--****--**---**--\
*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-\
*--*---*---**---**--****-***--***----*---**---***-\
*--*---*--*-------*----*----*-*--*--*---*--*----*-\
-**---***-****-***-----*-***---**---*----**---**--\
--------------------------------------------------\
'''

digitpinch = 5
rowpinch = digitpinch * 10
digitheight = 6

f = open(sys.argv[1], 'r')
for line in f:
    if not line.strip():
        continue
    for row in range(0, digitheight):
        for c in line:
            if not c.isdigit():
                continue
            ifrom = row * rowpinch + int(c) * digitpinch
            ito = ifrom + digitpinch
            print(digitsmap[ifrom: ito], end='')
        print('')
f.close()
