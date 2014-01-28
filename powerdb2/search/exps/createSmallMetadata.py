import os
import sys
import ast

lines = open("../MetadataDump_flattened").readlines()

featureFile = open("matrix")
uuids = []
for line in featureFile.readlines():
	uuid = line.split(',')[0].strip()
	uuids.append(uuid)

outfile = open("smallMetadata","w")
for line in lines:
	point = ast.literal_eval(line.strip())
	if point["uuid"] not in uuids:
		continue
	else:
		outfile.write(str(line.strip()) + "\n")

outfile.close()	
