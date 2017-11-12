#!/usr/bin/python
# -*- coding: UTF-8 -*-

def product(x,y):
	'''Returns the product of a two number'''
	return x*y

def score(num):
	'''Judgment score'''
	num = num/10
	if num>=9 | num<=10:
		return "A"
	elif num>=8:
		return "B"
	elif num>=7:
		return "C"
	elif num>=6:
		return "D"
	elif num<6:
		return "F"

def year(num):
	'''Returns whether a year is a leap years'''
	if num%4==0 | num/100!=0 or num%400 == 0:
		return "is leap year!"
	else :
		return "is noleap year!"




if __name__ == '__main__':
	print year(90)