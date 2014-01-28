import os
import sys
from search import *

lines = open("smallMetadata").readlines()
def searchQuery(query,numResults):
	global lines
	results = parse_query(lines,query,numResults)
	for result in results:
		print result["Path"]

def main():
	searchQuery("sdh temp",20)
	print "Next search"
	searchQuery("sdh temp",40)

if __name__ == "__main__":
	main()
