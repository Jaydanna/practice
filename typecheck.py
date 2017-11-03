#!/usr/bin/python
# -*- coding: UTF-8 -*-

def display(num):
	print num,'is',
	if isinstance(num,(int,float,long,complex)):
		print 'a number of type:',type(num).__name__
	else:
		print 'not a number at all!'

display(033)
display(0.997)
display(3325465546546546546)
display(-5.2+1.9j)
display('alsdkf')