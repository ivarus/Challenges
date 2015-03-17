'''
Created on Feb 18, 2015

@author: Ivan Varus
'''

import sys

slangphrases = [', yeah!',
                ', this is crazy, I tell ya.',
                ', can U believe this?',
                ', eh?',
                ', aw yea.',
                ', yo.',
                '? No way!',
                '. Awesome!']

f = open(sys.argv[1], 'r')
add = 0
flag = False
for line in f:
    for c in line:
        target = c
        if c == '.' or c == '!' or c == '?':
            if flag:
                target = slangphrases[add % len(slangphrases)]
                add += 1
            flag = not flag
        print(target, end='')
    print('')
f.close()
