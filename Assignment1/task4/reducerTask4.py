#!/usr/bin/python3
import csv
import sys
from operator import itemgetter


dict1 = {}
li=[]
for line in sys.stdin:
    line = line.strip()
    line_val = line.split("\t")
    #print(line_val)
    k = line_val[0]
    val = line_val[1].split(",")
    
    
    bat = val[0]
    runs = int(val[1])

    if k in dict1:
       if bat in dict1[k]:
          dict1[k][bat][1] += 1
          dict1[k][bat][0] += runs
       else:
          dict1[k][bat]=[0,1]
          dict1[k][bat][0] += runs
    else:
       dict1[k] = {}
       dict1[k][bat] = [0,1]
       dict1[k][bat][0] += runs            


for k in list(dict1):
	for bat in list(dict1[k]):
		if dict1[k][bat][1] < 10:
        		del dict1[k][bat]


for key in dict1:
	for bat in dict1[key]:
		str_Rate = (dict1[key][bat][0]*100)/dict1[key][bat][1]
		dict1[key][bat].append(str_Rate)
		
for key in dict1:
	venue = key
	batsman = list(dict1[key].keys())[0]
	for bat in dict1[key]:
		if(dict1[key][bat][2] > dict1[key][batsman][2]):
			batsman = bat
		elif(dict1[key][bat][2] == dict1[key][batsman][2]):
			if(dict1[key][bat][0] > dict1[key][batsman][0]):
				batsman = bat
	li.append((venue,batsman))	
li.sort()
for i in range(len(li)):
	venue=(li[i][0])
	batsman=(li[i][1])
	print('%s,%s' % (venue,batsman))




