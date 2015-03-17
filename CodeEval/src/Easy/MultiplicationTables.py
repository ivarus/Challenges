'''
Created on Feb 11, 2015

@author: Ivan Varus
'''


if __name__ == '__main__':
    for i in range(1, 13):
        for j in range(1, 13):
            s = str(i*j)
            if j > 1:
                while len(s) < 4:
                    s = ' ' + s
            print(s, end='')
        print('')
