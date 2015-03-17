'''
Created on Feb 18, 2015

@author: Ivan Varus
'''

import sys

ages = [2, 4, 11, 14, 18, 22, 65, 100]
categories = ['Still in Mama\'s arms',
              'Preschool Maniac',
              'Elementary school',
              'Middle school',
              'High school',
              'College',
              'Working for the man',
              'The Golden Years']

f = open(sys.argv[1], 'r')
for line in f:
    if not line.strip():
        continue
    age = int(line)
    if age < 0 or age > 100:
        print('This program is for humans')
        continue
    for i in range(0, len(ages)):
        if age <= ages[i]:
            print(categories[i])
            break
f.close()
