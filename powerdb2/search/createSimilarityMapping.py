import os
import sys
import operator
import ast

uuids = []
def readUUIDFile():
	global uuids
	uuids = [ line.strip() for line in open("uuids").readlines() ]

def createSimCorr(filename):
	global uuids
	corr = {}
	top_corr = {}
	for uuid in uuids:
		corr[uuid] = {}
	lines = open(filename).readlines()
	print "Started reading correlations"
	count = 0
	for i in range(len(lines)):
		if lines[i].strip() == '':
			continue
		print "Doing for line :",i
		parts = lines[i].strip().split('\t')
		for j in range(len(parts)):

			if parts[j].strip() == 'nan' or parts[j].strip() == '0.0':
				continue
			c = float(parts[j].strip())
				
			corr[uuids[i]][uuids[i+1+j]] = c
			corr[uuids[i+1+j]][uuids[i]] = c

	print "Finished reading correlations"
	count = 0
	print "Started sorting correlations"
	for uuid in uuids:
		sorted_order = []
		if len(corr[uuid]) > 0:
			sorted_order = sorted(corr[uuid].iteritems(),key=operator.itemgetter(1),reverse=True)

		if len(sorted_order) >= 10:
			top_corr[uuid] = sorted_order[0:9]
		else:
			top_corr[uuid] = []
		if count % 100 == 0:
			print "Done ",count
		count += 1

	outfile = open("CorrMatSDH","w")
	for uuid in top_corr:
		print uuid,":",top_corr[uuid]
		point = {}
		point[uuid] = top_corr[uuid]
		outfile.write(str(point) + "\n")

	outfile.close()

def createSimMetadata():
	global uuids
	points = {}
	lines = open("MetadataDump_flattened").readlines()
	for line in lines:
		point = ast.literal_eval(line.strip())
		points[point["uuid"]] = point

	sim = {}
	for uuid in uuids:
		sim[uuid.strip()] = {}
	for i in range(len(uuids)):
		print "Doing point",i
		for j in range(i+1,len(uuids)):
			point_i = points[uuids[i]]
			point_j = points[uuids[j]]
			score = 0.0
			for key in point_i :
				if key in point_j:
					score += 0.5
					if point_j[key] == point_i[key]:
						score += 0.5	
	 
			sim[uuids[i]][uuids[j]] = score
			sim[uuids[j]][uuids[i]] = score

	top_sim = {}
	print "Started sorting"
	count = 0
	for uuid in uuids:
		sorted_order = []
		if len(sim[uuid]) > 0:
			sorted_order = sorted(sim[uuid].iteritems(),key=operator.itemgetter(1),reverse=True)

		if len(sorted_order) >= 10:
			top_sim[uuid] = sorted_order[1:100]
		else:
			top_sim[uuid] = []
		if count % 100 == 0:
			print "Done ",count
		count += 1

	print "Ended sorting"
	outfile = open("SimMetadataSDH","w")
	for uuid in top_sim:
		print uuid,":",top_sim[uuid]
		point = {}
		point[uuid] = top_sim[uuid]
		outfile.write(str(point) + "\n")

	outfile.close()

if __name__ == "__main__":
	readUUIDFile()
	#createSimCorr("PLAIN_corr")
	createSimMetadata()	
