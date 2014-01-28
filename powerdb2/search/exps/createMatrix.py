import os
import sys
import ast
import re

def readlines():
	global points
	lines = open("../MetadataDump_flattened").readlines()

	points = {}

	for j in range(len(lines)):
		if j % 1000 == 0:
			print "Done line ",j
		if "sample" in lines[j].strip() or "axis" in lines[j].strip() or "electricity-total" in lines[j].strip() or "sum" in lines[j].strip():
			continue
		if "sdh" not in lines[j].lower():
			continue
		point = ast.literal_eval(lines[j].strip())
		points[point["uuid"]] = {}
		points[point["uuid"]]["dict"] = point
		points[point["uuid"]]["dict-split"] = {}
		for key in points[point["uuid"]]["dict"]:
			if key == "uuid":
				split_values = []
				split_values.append(point["uuid"])
				points[point["uuid"]]["dict-split"][key] = split_values
				continue
			value = points[point["uuid"]]["dict"][key]
			split_values = re.split('\ |\/|\.|\_|\-|\,|\:',value)
			points[point["uuid"]]["dict-split"][key] = split_values
			if len(split_values) > 50 :
				print lines[j].strip(),"\n\n"
		points[point["uuid"]]["index"] = j

def initializeFields():
	global fields
	fields = {}
	lines = open("fields").readlines()
	for line in lines:
		fieldname = line.strip()[1:-2]
		fields[fieldname] = []

def maxSplits():
	global fields
	global points

	print "calculating max splits"
	count = 0
	for uuid in points:
		if count % 1000 == 0:
			print "Done line ",count
		for key in points[uuid]["dict-split"]:
			length = len(points[uuid]["dict-split"][key])
			if length not in fields[key]:
				fields[key].append(length)
		count += 1

	for field in fields:
		print field,"\t\t",fields[field]

def fillMatrix():
	global points
	global fields

	print "filling Matrix"
	matrix = []
	allFields = []
	allFields.append("uuid-0")
	for field in fields:
		if len(fields[field]) == 0 or field=="uuid":
			continue

		#print field,fields[field]
		#print max(fields[field])
		for i in range(max(fields[field])):
			allFields.append(field+"-"+str(i))

	for uuid in points:
		point = {}
		point_orig = points[uuid]["dict-split"]
		for key in point_orig:
			for i in range(len(point_orig[key])):
				point[key+"-"+str(i)] = point_orig[key][i]

		point_row = []
		for field in allFields:
			if field not in point:
				point_row.append("")
			else:
				point_row.append(point[field])

		matrix.append(point_row)

	print "Outputing file"
	outputfile = open("matrix","w")
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			outputfile.write(str(matrix[i][j]) + ",")
		outputfile.write("\n")


	outputfile.close()
	fieldsFile = open("fieldsFile","w")
	for i in range(len(allFields)):
		fieldsFile.write(allFields[i].strip() + "\n")

	fieldsFile.close()

if __name__ == "__main__":
	readlines()
	initializeFields()
	maxSplits()		
	#fillMatrix() 
