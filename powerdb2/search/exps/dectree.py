import sys
import os
from sklearn.svm import SVC	
import numpy
from sklearn import tree
import StringIO, pydot 
import re
import ast
from search import *
from sklearn.feature_extraction import DictVectorizer

def readlines():
	global lines
	global features
	global points
	lines = open("smallMetadata").readlines()

	points = {}
	for line in lines:
		point = ast.literal_eval(line.strip())
		points[point["uuid"]] = point

	features = {}
	feature_lines = open("matrix").readlines()
	fields_lines = open("fieldsFile").readlines()

	for line in feature_lines:
		parts = line.split(',')
		point = {}
		for i in range(len(fields_lines)):
			point[fields_lines[i].strip()] = parts[i].strip()


		
		#parts = line.strip().split(',')
		uuid = parts[0].strip()
		features[uuid] = point
		
	

def searchQuery(query,numResults):
	global lines
	results = parse_query(lines,query,numResults)
	#for point in results:
	#	print point["Path"]
	print "Number of results : ",len(results)
	return results

def runDecTree(query):

	global features
	global points  
	clf = tree.DecisionTreeClassifier()
	results = searchQuery(query,100000)
	
	Training = []
	ClassNames = []
	for result in results:
		if "RAT" in str(result) in str(result):
			Training.append(features[result["uuid"]])
			ClassNames.append(1)
			print result
		else:
			Training.append(features[result["uuid"]])
			ClassNames.append(0)

	#print Training
	#print "\n\n\n\n\n\n"
	v = DictVectorizer(sparse=False)
	Training = v.fit_transform(Training)
	
	#print v.inverse_transform(Training)
	
	#print Training.size

	#print Training
	#return

	names = v.get_feature_names()
	for i in range(len(names)):
		print i,names[i]

	clf.fit(Training[:100],ClassNames[:100])
	dot_data = StringIO.StringIO()
	tree.export_graphviz(clf, out_file=dot_data) 
	graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
	graph.write_pdf("tree.pdf") 

	count = 0
	for i in range(len(results)):
		#print 
		output = clf.predict(Training[i])
		#print output
		if output[0] == 1:
			print results[i]["Path"]
			count += 1

	print "Total number of returned results : ",count
	print clf
	print dot_data.getvalue()
if __name__ == "__main__":
	readlines()
	query = ""
	for word in sys.argv[1:]:
		query = query + word + " "
	query = query.strip()

	#searchQuery(query)
	runDecTree(query)
