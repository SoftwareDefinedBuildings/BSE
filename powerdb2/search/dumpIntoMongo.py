from pymongo import MongoClient
import sys
import ast

def dump():
	client = MongoClient()

	filename = open("MetadataDump")

	db = client.smap_db

	smap_db = db.metadata
	count = 0
	for line in filename.readlines():
		d = ast.literal_eval(line.strip())
		key_names = getKeyNames(d,[],'')
		d['keynames'] = key_names
		#print d
		smap_db.insert(d)
		count += 1
		if count % 1000 == 0:
			print "Done ",count,"lines"
	
def getKeyNames(d,l,prefix):
	for key in d:
		l.append(str(prefix) + str(key))
		if type(d[key]) is dict:
			getKeyNames(d[key],l,str(prefix) + str(key) + "/")

	return l

if __name__ == "__main__":
	dump()
