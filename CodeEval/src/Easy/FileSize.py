'''
Created on Feb 12, 2015

@author: Ivan Varus
'''


import sys

if __name__ == '__main__':
    f = open(sys.argv[1], 'rb')
    if not f:
        exit(1)
    f.seek(0, 2)
    print(f.tell())
    f.close()
