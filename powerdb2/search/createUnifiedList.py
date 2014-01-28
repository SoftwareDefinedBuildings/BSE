import os
import sys
import ast

def unify(filename1,filename2):
	points = {}
	lines1 = open(filename1).readlines()
	lines2 = open(filename2).readlines()
	for line in lines1:
		point = ast.literal_eval(line.strip())
		for uuid in point:
			points[uuid] = point[uuid]

	for line in lines2:
		point = ast.literal_eval(line.strip())
		for uuid in point:
			points[uuid].extend(point[uuid])

	outfile = open("finalSim","w")
	for point in points:
		p = {}
		p[point] = points[point]
		outfile.write(str(p) + "\n")

	outfile.close()

if __name__ == "__main__":
	unify("SimMetadataSDH","CorrMatSDH")

	
