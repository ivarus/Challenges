'''
Created on Feb 20, 2015

@author: Ivan Varus
'''

import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    test = test.strip()
    if not test:
        continue
    num = int(test)
    checked = set()
    while True:
        if num == 1:
            print('1')
            break
        num = sum(int(c) ** 2 for c in str(num))
        if num in checked:
            print('0')
            break
        checked.add(num)
test_cases.close()
