import os
import sys
from get_corr import *
from datetime import datetime
import numpy
data = {}
uuids = []
def readAllData():
	global uuids
	global data
	uuids = open("uuids").readlines()
	start = datetime.now()
	for uuid in uuids:
		uuid = uuid.strip()
		f = open("data/" + uuid.strip())
		lines = f.readlines()
		r = []
		for line in lines:
			r.append(float(line.strip().split('\t')[1].strip()))
		readings = numpy.array(r)
		data[uuid] = readings

def getEMDCorr():
	global uuids
	global data
	count = 0
	total = len(uuids) * len(uuids)/2
	start = datetime.now()
	outfile = open("EMD_corr","w")
	for i in range(len(uuids)):
		for j in range(i+1,len(uuids)):
			ts1 = data[uuids[i].strip()]
			ts2 = data[uuids[j].strip()]
			print ts1
			print ts2
			c = get_corr(ts1,ts2,1)
			outfile.write(str(c) + "\t")

			'''
			try:
				c = get_corr(ts1,ts2,1)
				outfile.write(str(c) + "\t")
			except Exception as inst:
				outfile.write(str("EX") + "\t")
				print type(inst)
				print inst.args
				print inst
			'''
			if count % 1000 == 0:
				print "Done",float(count)*1000.0/total," Took : ",(datetime.now()-start).seconds,"secs"
			count += 1
		outfile.write("\n")
		print "Finished finding correlation for ",i
	
if __name__ == "__main__":
	readAllData()
	getEMDCorr()
