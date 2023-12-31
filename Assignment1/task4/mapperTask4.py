#!/usr/bin/python3
import sys
import csv
venue = ''
for line in sys.stdin:
	line = line.strip()
	li = line.split(',')
	if(li[0] == 'info' and li[1] == 'venue'):
		venue = li[2]
	elif(li[0] == "ball"):
		key_list = venue
		val_list = li[4]+','+li[7]
		print('%s\t%s' % (key_list,val_list))  
