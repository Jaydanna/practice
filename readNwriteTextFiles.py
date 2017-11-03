#! /usr/bin/python
# -*- coding: UTF-8 -*-

import os
ls = os.linesep

while True:
	print '''1..makeTextFile  2.readTextFile  3.quit  ''' 
	choose = int(raw_input('please your choose:'))
	if choose == 1:
		# makeTextFile.py -- create text file
		fname = raw_input('input:')
		#get filename
		while True:
			if os.path.exists(fname):
				print "ERROR:'%s' already exits" % fname
			else:
				break
		all = []
		print "\nEnter lines('.'by itself to quir).\n"

		#loop until user terminates input
		while True:
			entry = raw_input('>')
			if entry == '.':
				break
			else:
				all.append(entry)

		#write lines to file with proper line=ending
		fobj = open(fname,'w')
		fobj.writelines(['%s%s' % (x,ls)for x in all])
		fobj.close()
		print 'DONE!'
		print '%s',type(ls)

	elif choose == 2:
		#get filename
		fname = raw_input('Enter:')
		try:
			fobj = open(fname,'r')
		except IOError,e:
			print "***file open error:",e
		else:
			#display contents to the screen
			for eachLine in fobj:
				print eachLine.strip()
			fobj.close()
	else:
		break