import sys
import os
import ast

lines = open("MetadataDump").readlines()
outfile = open("uuids","w")
count = 0
total = len(lines)
for line in lines:
	point = ast.literal_eval(line.strip())
	uuid = point["uuid"]
	if "Metadata" in point:
		if "SourceName" in point["Metadata"]:
			if point["Metadata"]["SourceName"] == "Sutardja Dai Hall BACnet":
				outfile.write(str(uuid) + "\n")
	if count % 10000 == 0:
		print "Done ", float(count)*100.0/total
	count += 1

outfile.close()

