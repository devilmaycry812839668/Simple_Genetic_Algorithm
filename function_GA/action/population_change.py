#!/usr/bin/env python
#encoding:UTF-8

import random

#变异
def change_fun(s, belta):

    def in_action():
        j = random.randint(0, len(s)*len(s[0])-1)

        i = j/len(s[0])
        j = j%len(s[0])

        if j != 0 and j!= len(s[0])-1:
            if s[i][j] == '0':
                s[i] = s[i][0:j]+'1'+s[i][j+1:]
            else:
                s[i] = s[i][0:j]+'0'+s[i][j+1:]
        elif j == 0:
            if s[i][j] == '0':
                s[i] = '1'+s[i][j+1:]
            else:
                s[i] = '0'+s[i][j+1:]
        else:
            if s[i][j] == '0':
                s[i] = s[i][0:j]+'1'
            else:
                s[i] = s[i][0:j]+'0'
 
    for x in xrange(int( len(s[0])*len(s)*belta )):
	in_action()

    #in_action()
	   
