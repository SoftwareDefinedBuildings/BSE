import os
import sys
from smap.archiver.client import SmapClient
from get_corr import *

c = SmapClient("http://www.openbms.org/backend")
timeseries = {}

def getTimeSeries():
	global c
	uuids = open("uuids").readlines()
	count = 0
	total = len(uuids)
	for i in range(len(uuids)):
		data = c.query('apply window(mean,field="minute",width=15) to data in ("12/1/2012","12/2/2012") where uuid="' + str(uuids[i].strip()) + '"')
		f = open("data/" + uuids[i].strip(),"w")
		for reading in data[0]["Readings"]:
			f.write(str(reading[0]/1000) + "\t" + str(reading[1])+"\n") 
		f.close()
		if count % 100 == 0:
			print "Done ",float(count)*100.0/total

		count += 1

if __name__ == "__main__":
	getTimeSeries()

