'''
Created on Feb 12, 2015

@author: Ivan Varus
'''

import sys


def str2sec(s):
    hhmmss = s.split(':')
    if len(hhmmss) != 3:
        return None
    sec = int(hhmmss[0]) * 3600 + int(hhmmss[1]) * 60 + int(hhmmss[2])
    return sec


def sec2str(sec):
    hh = sec // 3600
    mm = sec % 3600 // 60
    ss = sec % 60
    return '{:02}:{:02}:{:02}'.format(hh, mm, ss)


f = open(sys.argv[1], 'r')
for line in f:
    ab = line.split()
    if len(ab) != 2:
        pass
    asec = str2sec(ab[0])
    bsec = str2sec(ab[1])
    d = abs(asec - bsec)
    print(sec2str(d))
f.close()
