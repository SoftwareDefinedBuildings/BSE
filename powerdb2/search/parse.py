import os
import sys
import re
import ast

uuid = 0
def getData(pointname,d):
	global uuid
	data = {}
	flag = 0
	data = d

	if "SDH" not in pointname:
		return data
		
	if "SDH" in pointname:
		data["building"] = "SDH"
		flag = 1

	if "AIR VOLUME" in pointname:
		data["subsystem"] = "VAV"
		data["subsystemid"] = pointname.split('.')[1].strip()
		data["type"] = "AIR VOLUME"
		flag = 1
	elif "ROOM TEMP" in pointname:
		data["subsystem"] = "VAV"
		data["subsystemid"] = pointname.split('.')[1].strip()
		data["type"] = "ROOM TEMP"
		flag = 1

	elif "AH" in pointname:
		data["subsystem"] = "AIR HANDLER"
		data["subsystemid"] = re.split('\.|\_|\ ',pointname)[1].strip()
		data["type"] = re.split('\.|\_|\ ',pointname)[2].strip()
		#print pointname,data
		flag = 1

	elif "CH" in pointname:
		data["subsystem"] = "CHILLER"
		data["subsystemid"] = re.split('\.|\_|\ ',pointname)[1].strip()
		data["type"] = re.split('\.|\_|\ ',pointname)[2].strip()
		flag = 1

	elif "HW" in pointname:
		data["subsystem"] = "HOT WATER PUMP"
		data["subsystemid"] = re.split('\.|\_|\ ',pointname)[1].strip()
		data["type"] = re.split('\.|\_|\ ',pointname)[2].strip()
		flag = 1


	elif "DEM" in pointname:
		data["subsystem"] = "POWER METER"
		data["meterType"] = "DEM"
		data["powerType"] = re.split('\.|\_|\ ',pointname)[-1].strip()
		data["subsystemid"] = re.split('\.|\_|\ ',pointname)[1].strip()
		flag = 1

	elif ".SW." in pointname:
		data["subsystem"] = "POWER METER"
		data["meterType"] = "SW"
		data["powerType"] = re.split('\.|\_|\ ',pointname)[-1].strip()
		data["subsystemid"] = re.split('\.|\_|\ ',pointname)[1].strip()
		flag = 1

	elif ".WIN." in pointname:
		data["subsystem"] = "WINDOW"
		data["subsystemid"] = re.split('\.|\_|\ ',pointname)[2].strip()
		data["type"] = re.split('\.|\_|\ ',pointname)[-1].strip()
		flag = 1

	if flag == 1:
		print "Modified for path ",pointname
	return data

def readPoints(filename):
	global uuid
	global data
	lines = open(filename).readlines()
	outfile = open(filename + ".modified","w")
	count = 0
	for line in lines[0:]:
		d = ast.literal_eval(line.strip())
		path = d['Path']
		#print d
		newPathName = re.sub('/','.',path)
		finalDict = getData(newPathName,d)
		if finalDict != d:
			print " dict for ",path," changed"
		outfile.write(str(finalDict) + "\n")
		count += 1
		if count % 100 == 0:
			print "Done line ",count

	
		

if __name__ == "__main__":
	readPoints(sys.argv[1])
