#!/usr/bin/python
# -*- coding: UTF-8 -*-

def pyment(monnum):
	initnum = 0
	i = 0
	maxnum = int(raw_input("Enter opening balance: "))
	print "Amount Remaining"
	print "Pymt# Paid Balance"
	print "----- ------ ---------"

	while (monnum < maxnum):
		balance = maxnum - monnum
		print "'%d     $'%d'     $'%d'"% (i,monnum,balance)
		i+=1


if __name__ == '__main__':
	monnum = int(raw_input("Enter monthly payment: "))
	pyment(monnum)