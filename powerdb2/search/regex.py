from smap.archiver.client import SmapClient
from smap.contrib import dtutil

from matplotlib import pyplot
from matplotlib import dates
import os
import re
import json
import ast
from datetime import datetime

# make a client
c = SmapClient("http://new.openbms.org/backend")

# get tag list
#tag = [i.strip('\n') for i in open('tagList.txt', 'r').readlines()]
stnc = "select distinct Path"
result = c.query(stnc)

outFile = open("MetadataDump","w")
finalStructure = {}
count = 0
lastTime = datetime.now()
print len(result)
print "Experiment started at : ",lastTime
for tag in result:
	queryString = "select * where Path='" + tag + "'"
	out = c.query(queryString)
	#finalStructure[tag] = out[0]
	count += 1
	if count % 100 == 0:
		timeNow = datetime.now()
		timeTaken = (timeNow - lastTime).seconds
		print "Done ... ",float(count)*100.0/len(result),"% Time taken : ",timeTaken,"seconds. Time now ",timeNow
		lastTime = timeNow
	try:
		outFile.write(str(out[0]) + "\n")
	except:
		print out
		continue
	
#json.dump(finalStructure,outFile)


print len(result)


#prompt user to input
#input = raw_input("keyword to query: ")

# regular expression search goes here...
# kw = input.split(' ')
# regex = re.compile("(?i).*(name).*")
# entry = [m.group(0) for l in tag for m in [regex.search(l)] if m]
# for e in entry:
'''
for e in tag:
	# stnc = "select distinct Path where %s like '%%%s%%'"%(e, input)
	stnc = "select distinct Path where %s ~ '(?i).*%s.*'"%(e, input)
	print ">>>>>>>>>>query with entry %s>>>>>>>>>>"%e
	list = c.query(stnc) #the result is a list
	if list:
		print "the entry getting matches is", e
		print '\n'.join(i for i in list)
'''
