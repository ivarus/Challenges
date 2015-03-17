'''
Created on Mar 5, 2015

@author: Ivan Varus
'''

import sys
import re
from collections import Counter


def convertDotted(s, b):
    return tuple(int(e, b) for e in s.split('.'))


def convertPlain(s, b):
    bs = '{:0>32}'.format(bin(int(s, b))[2:])
    return tuple(int(bs[i*8:(i+1)*8], 2) for i in range(4))


patterns = {
    # dotted
    (re.compile(r'((?:[01]{8}\.){3}[01]{8})'), convertDotted, 2),
    (re.compile(r'((?:0[07]{3}\.){3}0[07]{3})'), convertDotted, 8),
    (re.compile(r'((?:\d{1,3}\.){3}\d{1,3})'), convertDotted, 10),
    (re.compile(r'((?:0x[a-f\d]{2}\.){3}0x[a-f\d]{2})', re.I), convertDotted, 16),
    # plain
    (re.compile(r'([01]{32})'), convertPlain, 2),
    (re.compile(r'(0[07]{11})'), convertPlain, 8),
    (re.compile(r'(\d{10})'), convertPlain, 10),
    (re.compile(r'(0x[a-f\d]{8})', re.I), convertPlain, 16),
}


def findMostCommonIPs(f):
    ips = Counter()
    for line in f:
        for pattern, convertFunc, base in patterns:
            for match in re.findall(pattern, line):
                ip = convertFunc(match, base)
                if (1, 0, 0, 0) <= ip <= (255, 255, 255, 254):
                    ips[ip] += 1
    maxCount = ips.most_common(1)[0][1]
    return sorted(k for k, v in ips.items() if v == maxCount)


f = open(sys.argv[1], 'r')
ips = findMostCommonIPs(f)
print(' '.join('.'.join(map(str, ip)) for ip in ips))
f.close()
