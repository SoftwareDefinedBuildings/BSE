import sys
import os
from sklearn.svm import SVC	
import numpy
from sklearn import tree
import StringIO, pydot 
import re
orientations = {'NORTH' : 1 , 'WEST' : 2 , 'EAST' : 3, 'SOUTH' : 4 , 'INTERIOR' : 5 }
weights = { 1: 1 , 2 : 1, 3: 1, 4 : 1, 5 : 1}
floorNames_test = []
floorNames_train = []
sample_weights = []
def makeTrainingSet(trainingFile,classFile):
	global floorNames_test
	global floorNames_train
	global sample_weights
	lines_train = open(trainingFile).readlines()
	for line in lines_train:
		line = re.sub( '\s+', ' ', line )
	lines_class = open(classFile).readlines()
	training = []
	classes = []
	test = []
	answers = []
	numTraining = {}
	for i in range(len(lines_class)):
		o = lines_class[i].strip().split(',')[1].strip().split(' ')[0].strip()
		features = []

		if o not in numTraining:
			numTraining[o] = 0
		if numTraining[o] >= 1000:
			parts = lines_train[i].strip().split(' ')
			for j in range(len(parts)):
				features.append(float(parts[j]))
			test.append(features)
			floorNames_test.append(lines_class[i].strip().split(',')[0].strip())
			answers.append(orientations[o])
			continue
		else:
			parts = lines_train[i].strip().split(' ')
			if len(parts) < 100:
				continue
			for j in range(len(parts)):
				features.append(float(parts[j]))

			print "Number of features : ",len(parts),lines_class[i]
			numTraining[o] += 1
			training.append(features)
			floorNames_train.append(lines_class[i].strip().split(',')[0].strip())
			classes.append(orientations[o])
			sample_weights.append(weights[orientations[o]])
			continue

	return (numpy.array(training),numpy.array(classes),numpy.array(test),numpy.array(answers))
		

def runSVM(TrainingFile,ClassNamesFile):
	global orientations
	global weights
	global floorNames_test
	global floorNames_train
	global sample_weights
	(Training,ClassNames,Test,Answers) = makeTrainingSet(TrainingFile,ClassNamesFile)

	#print Training
	print ClassNames
	#clf = SVC(kernel='linear')
	clf = tree.DecisionTreeClassifier()
	
	clf.fit(Training,ClassNames)
	dot_data = StringIO.StringIO()
	tree.export_graphviz(clf, out_file=dot_data) 
	graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
	graph.write_pdf("tree.pdf") 
	
	answers = {}
	floors = {}
	total_correct = 0
	total_incorrect = 0


	print "TRAINING SET :"
	
	for i in range(len(Training)):
		ans = clf.predict(Training[i])
		floor = floorNames_train[i]
		if ClassNames[i] not in answers:
			answers[ClassNames[i]] = {}
			answers[ClassNames[i]]["correct"] = 0
			answers[ClassNames[i]]["incorrect"] = 0
		
		if floor not in answers[ClassNames[i]]:
			answers[ClassNames[i]][floor] = {}
			answers[ClassNames[i]][floor]["correct"] = 0
			answers[ClassNames[i]][floor]["incorrect"] = 0
			answers[ClassNames[i]][floor]["total"] = 0

		if ans != ClassNames[i]:
			total_incorrect += 1
			answers[ClassNames[i]]["incorrect"] += 1
			answers[ClassNames[i]][floor]["incorrect"] += 1
			answers[ClassNames[i]][floor]["total"] += 1
			#print ans," - ",ClassNames[i]
		else:
			#print ans," - ",ClassNames[i]
			answers[ClassNames[i]]["correct"] += 1
			total_correct += 1
			answers[ClassNames[i]][floor]["correct"] += 1
			answers[ClassNames[i]][floor]["total"] += 1

	print "Number of correct predictions :",total_correct
	print "Number of incorrect predictions :",total_incorrect

	print "\n\n"

	for o  in answers:
		x = ''
		for name in orientations:
			if str(orientations[name.strip()]).strip() == str(o).strip():
				x = name
				break
		print x, " Correct :",answers[o]["correct"] ," Incorrect :",answers[o]["incorrect"]
		for floor in answers[o]:
			if "correct" in floor:
				continue
			print floor, " % Correct ",(answers[o][floor]["correct"] * 100) / answers[o][floor]["total"]

		print "\n\n"
	

	answers = {}
	floors = {}
	total_correct = 0
	total_incorrect = 0

	print "TEST SET"
	for i in range(len(Test)):
		ans = clf.predict(Test[i])
		floor = floorNames_test[i]
		if Answers[i] not in answers:
			answers[Answers[i]] = {}
			answers[Answers[i]]["correct"] = 0
			answers[Answers[i]]["incorrect"] = 0
		
		if floor not in answers[Answers[i]]:
			answers[Answers[i]][floor] = {}
			answers[Answers[i]][floor]["correct"] = 0
			answers[Answers[i]][floor]["incorrect"] = 0
			answers[Answers[i]][floor]["total"] = 0

		if ans != Answers[i]:
			total_incorrect += 1
			answers[Answers[i]]["incorrect"] += 1
			answers[Answers[i]][floor]["incorrect"] += 1
			answers[Answers[i]][floor]["total"] += 1
			#print ans," - ",ClassNames[i]
		else:
			#print ans," - ",ClassNames[i]
			answers[Answers[i]]["correct"] += 1
			total_correct += 1
			answers[Answers[i]][floor]["correct"] += 1
			answers[Answers[i]][floor]["total"] += 1

	print "Number of correct predictions :",total_correct
	print "Number of incorrect predictions :",total_incorrect

	print "\n\n"

	for o  in answers:
		x = ''
		for name in orientations:
			if str(orientations[name.strip()]).strip() == str(o).strip():
				x = name
				break
		print x, " Correct :",answers[o]["correct"] ," Incorrect :",answers[o]["incorrect"]
		for floor in answers[o]:
			if "correct" in floor:
				continue
			print floor, " % Correct ",(answers[o][floor]["correct"] * 100) / answers[o][floor]["total"]

		print "\n\n"



if __name__ == "__main__":
	runSVM(sys.argv[1],sys.argv[2])

