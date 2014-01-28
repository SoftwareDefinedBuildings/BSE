import os
import sys
from datetime import datetime

def testMemSpeed(query):
	lines = open("MetadataDump").readlines()
	now = datetime.now()
	words = query.split(" ")
	result = []
	for line in lines:
		flag = 0
		for word in words:
			word = word.strip()
			if word not in line:
				flag = 1
				break

		if flag == 0:
			result.append(line)

	finish = datetime.now()
	print "Time taken : ",finish-now

if __name__ == "__main__":
	testMemSpeed(sys.argv[1])
