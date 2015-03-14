'''
Created on Feb 21, 2015

@author: Ivan Varus
'''

import sys


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    pretty = test.strip()
    chunks = pretty.split(',')
    if len(chunks) == 0:
        continue
    words = []
    digits = []
    for chunk in chunks:
        if chunk.isdigit():
            digits.append(chunk)
        else:
            words.append(chunk)
    if len(digits) == 0 or len(words) == 0:
        print(pretty)
    else:
        print(','.join(words) + '|' + ','.join(digits))
test_cases.close()
