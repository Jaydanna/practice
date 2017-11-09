#!/usr/bin/python
# -*- coding: UTF-8 -*-

def product(x,y):
	'''Returns the product of a two number'''
	return x*y

def score(num):
	'''Jdgment score'''
	if num>=90 and num<=100:
		return "A"
	elif num>=80:
		return "B"
	elif num>=70:
		return "C"
	elif num>=60:
		return "D"
	elif num<60:
		return "F"

def year(num):
	'''Returns whether a year is a leap years'''
	if num%4==0 and num/100!=0 or num%400 == 0:
		return "is leap year!"
	else :
		return "is noleap year!"
def resl(num):
	while num < 100:
		if num >= 25 and num < 100:
			num25 = divmod(num, 25)
			print "got 25 is '%s'" % num25[0]
			if num25[1] >= 10 and num25[1] < 25:
				num10 = divmod(num25[1],10)
				print "got 10 is '%s'" % num10[0]
				if num10[1] >= 5 and num10[1] < 10:
					num5 = divmod(num10[1],10)
					print "got 5 is '%s'" % num5[0]
					if num5[1] >= 1 and num5[1] < 5:
						num1 = num5[1]
						print "got 1 is '%s'" % num1

				else:
					break
			else:
				break



if __name__ == '__main__':
	print resl(5)