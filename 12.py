#!/usr/bin/python
# -*- coding: UTF-8 -*-

def evennumber():  
   num = [0:21]
   if C == 1 :
   		for i in range(0,21):
    		if num[i] % 2 == 0:
    			return num[i]
    			i+=1
    elif C == 0:
    	for i in range(0,21):
    		if num[i] % 2 != 0:
    			return num[i]
    			i+=1
    else:
    	print 'WRONG~#$@,ONLY 1 OR 0~'

if __name__ == '__main__':
	C = raw_input('what do you want:')
