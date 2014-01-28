# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect, HttpResponseBadRequest, Http404
from django.contrib.admin import site as adminsite
from search import * 
import re
import ast
from sklearn.svm import SVC	
import numpy
from sklearn import tree
import StringIO, pydot 
import re
import ast
from search import *
from sklearn.feature_extraction import DictVectorizer


i = 0
lines = open("search/smallMetadata").readlines()

points = {}

for j in range(len(lines)):
	point = ast.literal_eval(lines[j].strip())
	points[point["uuid"]] = {}
	points[point["uuid"]]["string"] = lines[j].strip()
	points[point["uuid"]]["dict"] = point
	#points[point["uuid"]]["dict-split"] = {}
	#for key in points[point["uuid"]]["dict"]:
	#	value = points[point["uuid"]]["dict"][key]
	#	split_values = re.split('\ |\/|\.|\_|\-|\,',value)
	#	points[point["uuid"]]["dict-split"][key] = split_values
	points[point["uuid"]]["index"] = j
	if j==0:
		print points

similarity = {}
for line in open("search/finalSim").readlines():
	point = ast.literal_eval(line.strip())
	for uuid in point:
		similarity[uuid] = point[uuid]
	#print similarity

features = {}
feature_lines = open("search/matrix").readlines()
fields_lines = open("search/fieldsFile").readlines()

for line in feature_lines:
	parts = line.strip().split(',')
	point = {}
	for i in range(len(fields_lines)):
		point[fields_lines[i].strip()] = parts[i].strip()	
	uuid = parts[0].strip()
	features[uuid] = point
	

def search(request):
    t = loader.get_template('search3.html')
    c = Context({})
    return HttpResponse(t.render(c))

def getresultsStatus(request):
	global i
	global lines

	f = open("temp-" + str(i),"w")
	#f.write(str(request))
	i += 1
	f.write("SESSION DATA : " + str(request.session))

	request.session["test_key"] = "TEST VALUE"

	f.write("\n\n\nNEW SESSION DATA\n" + str(request.session) + "\n\n")
	parts = str(request).split(',')
	result = [ ]
	for part in parts:
		if "POST" not in part:
			continue
		#f.write(" Number of lines in read file : " + str(len(lines)))
		query = part.strip().split('\'')[1].strip()
		result = parse_query(lines,query,20)	

		if len(result) == 0:
			result = [ {"Path" : "No results" } ]
		#f.write("\n\n"  + str(query) + "\n\n" + str(result))
		break
	#f.close()	

	deleted_flag = []
	for j in range(len(result)):
		deleted_flag.append(1)

	request.session["displayed_search_results"] = result
	if "all_search_results" in request.session:
		del request.session["all_search_results"]
	#request.session["result_counter"] = len(result)
	request.session["deleted"] = 0
	request.session["deleted_results"] = []

	result = str(result)
	result = re.sub('\'','\"',result)
	return HttpResponse([result])

def getExtraResults(request):
	global i
	global lines

	#f = open("temp-" + str(i),"w")
	#f.write(str(request))
	#i += 1


	parts = str(request).split(',')
	result = [ ]
	for part in parts:
		if "POST" not in part:
			continue
		#f.write(" Number of lines in read file : " + str(len(lines)))
		query = part.strip().split('\'')[1].strip()
		result = parse_query(lines,query,10000)	

			
		if len(result) == 0:
			result = [ {"Path" : "No results" } ]
		#f.write("\n\n"  + str(query) + "\n\n" + str(result))
		break
	#f.close()	
	
	final_results = []
	#final_results.extend(request.session["displayed_search_results"])
		
	for point in result:
		if point in request.session["displayed_search_results"] or point in request.session["deleted_results"]:
			continue
		final_results.append(point)
		
	request.session["all_search_results"] = final_results
	request.session.modified = True
	print "Obtained all search results, Number of results : ",len(request.session["all_search_results"])
	result = str(result)
	result = re.sub('\'','\"',result)
	return HttpResponse([result])


def getNextSearchResults(request):
	global features
	#counter = request.session["result_counter"]
	if len(request.session["all_search_results"]) == 0:
		result = str(request.session["displayed_search_results"])
		result = re.sub('\'','\"',result)
		print "No more search results to display"
		return HttpResponse([result])

	
	if (request.session["deleted"]) > 0 and len(request.session["displayed_search_results"]) > 0 :
		print "TRAINING DEC TREE"
		clf = tree.DecisionTreeClassifier()
		Training = []
		ClassNames = []
		for j in range(len(request.session["displayed_search_results"])):
			uuid = request.session["displayed_search_results"][j]["uuid"]
			Training.append(features[uuid])
			ClassNames.append(1)

		for j in range(len(request.session["deleted_results"])):
			uuid = request.session["deleted_results"][j]["uuid"]
			Training.append(features[uuid])
			ClassNames.append(0)


		for j in range(len(request.session["all_search_results"])):
			uuid = request.session["all_search_results"][j]["uuid"]
			Training.append(features[uuid])


		num_displayed = len(request.session["displayed_search_results"])
		num_deleted = len(request.session["deleted_results"])
		num_all_search_results = len(request.session["all_search_results"])

		v = DictVectorizer(sparse=False) 
		Training = v.fit_transform(Training)
		
		clf.fit(Training[:(num_displayed+num_deleted)],ClassNames) 
		more_results = []
		dot_data = StringIO.StringIO()
		tree.export_graphviz(clf, out_file=dot_data) 
		graph = pydot.graph_from_dot_data(dot_data.getvalue()) 
		graph.write_pdf("tree.pdf") 
		names = v.get_feature_names()
		for j in range(len(names)):
			print j,names[j]

		for j in range((num_displayed+num_deleted),(num_displayed+num_deleted+num_all_search_results)):
			prediction = clf.predict(Training[j])[0]
			if prediction == 1:
				more_results.append(request.session["all_search_results"][j-(num_displayed+num_deleted)])
			
		count = 0	
		print "Total number of results :",num_displayed+len(more_results)
		print "Total number of results removed in this iteration : ",num_all_search_results-len(more_results)
		for point in more_results:
			request.session["displayed_search_results"].append(point)
			request.session["all_search_results"].remove(point)
			count += 1
			if count == 20:
				break

		result = str(request.session["displayed_search_results"])
		result = re.sub('\'','\"',result)
		#print "DISPLAYED SEARCH RESULTS"
		#for point in request.session["displayed_search_results"]:
		#	print point["Path"]

		#print "DELETED RESULTS"
		#for point in request.session["deleted_results"]:
		#	print point["Path"]
		
		request.session.modified = True

		return HttpResponse([result])

	else:
		print "ALL RESULTS DELETED OR NO RESULTS DELETED"
		count = 0
		to_delete = []
		for point in request.session["all_search_results"]:
			request.session["displayed_search_results"].append(point)
			to_delete.append(point)
			count += 1
			if count == 20:
				break

		for point in to_delete:
			request.session["all_search_results"].remove(point)
		
		result = str(request.session["displayed_search_results"])
		print "Number of displayed search results : ",len(request.session["displayed_search_results"])
		result = re.sub('\'','\"',result)
		request.session.modified = True
		return HttpResponse([result])


def replace(request):
	global points
	global i
	global similarity
	#f = open("temp-" + str(i),"w")
	#f.write(str(request))
	#i += 1
	parts = str(request).split(',')
	ans = [ ]

	result = []
	point_to_remove = None
	index = 0
	for part in parts:
		if "POST" not in part:
			continue
		query = part.strip().split('\'')[1].strip()
		print query
		#point_to_remove = None
		for point in request.session["displayed_search_results"]:
			if query == point["uuid"]:
				print "Removing point ",point
				point_to_remove = point
				break
		break

	print "Number of displayed search results : ",len(request.session["displayed_search_results"])
	#request.session["all_search_results"].remove(point_to_remove)
	#request.session["result_counter"] -= 1
	request.session["deleted"] += 1
	request.session["deleted_results"].append(point_to_remove)
	request.session["displayed_search_results"].remove(point_to_remove)
	request.session.modified = True
	#request.session["deleted_flag"][index] = 0

	return HttpResponse("")

def genQuery(request):
	#counter = request.session["result_counter"]
	global features
	common_keys = []
	ref_point = features[request.session["displayed_search_results"][0]["uuid"]]
	for key in ref_point:
		flag = 0
		for orig_point in request.session["displayed_search_results"][1:len(request.session["displayed_search_results"])]:
			point = features[orig_point["uuid"]]
			if key not in point:
				flag = 1
				break
			if ref_point[key] != point[key]:
				flag = 1
				break
		
		if flag == 0:
			common_keys.append(key)

	query = "select data before now limit 1000 where "
	for k in range(len(common_keys)):
		if "UnitofMeasure" in common_keys[k]:
			continue
		if ref_point[common_keys[k]] == '':
			continue
		query = query + common_keys[k].split('-')[0].strip() + "~'" + ref_point[common_keys[k]] + "'"
		if k < len(common_keys)-1:
			query = query + " and "
	return HttpResponse(query)

def getSimilar(request):
	global points
	global i
	global similarity
	#f = open("temp-" + str(i),"w")
	#f.write(str(request))
	i += 1
	parts = str(request).split(',')
	ans = [ ]

	result = []
	for part in parts:
		if "POST" not in part:
			continue
		query = part.strip().split('\'')[1].strip()
		if query not in similarity:	
			break
		sim = similarity[query]
		for p in sim:
			point = points[p[0]]["dict"]
			result.append(point)

		break
	if len(result) == 0:
		result = [ {"Path" : "No results" } ]
	result = str(result)
	result = re.sub('\'','\"',result)
	return HttpResponse([result])


def replaceOld(request):
	global points
	global i
	global similarity
	#f = open("temp-" + str(i),"w")
	#f.write(str(request))
	i += 1
	parts = str(request).split(',')
	ans = [ ]

	result = []
	for part in parts:
		if "POST" not in part:
			continue
		query = part.strip().split('\'')[1].strip()
		if "test_key" not in request.session:
			result = [ { "Path" : " No results" , "uuid" : "random" } ]
		else:
			result = [ { "Path" : request.session["test_key"] , "uuid" : "random" } ]
		break
	result = str(result)
	result = re.sub('\'','\"',result)
	return HttpResponse([result])


		
def getMetadata(request):
	global points
	global i
	#f = open("temp-" + str(i),"w")
	#f.write(str(request))
	#i += 1
	parts = str(request).split(',')
	ans = [ ]
	for part in parts:
		if "POST" not in part:
			continue
		query = part.strip().split('\'')[1].strip()
		#f.write("\n UUID = " + query)
		print "UUID",query
		#ans = [ points['43a17dfe-3118-5cbe-b591-0178c9f95f5a']['string'] ]
		ans = [ str(points[query]["dict"]) ]
		#print "ANS ",ans
		#f.write("\n\n RETURNED " + str(ans))
		#f.close()
		break 
		
	return HttpResponse([ str(ans) ])

def updateMetadata(request):
	global points
	global lines
	global i
	#f = open("temp-" + str(i),"w")
	#f.write(str(request))
	#i += 1
	parts = str(request).split(',')
	ans = [ ]
	for part in parts:
		if "POST" not in part:
			continue
		query = part.strip().split('\'')[1].strip()

		print "UPDATING DATA",query
		tags = query.strip().split(' ')
		uuid = tags[0].strip()
		for tag in tags[1:]:
			key = tag.split(':')[0].strip()
			value = tag.split(':')[1].strip()
			points[uuid]["dict"]["Added/" + key] = value
		
		points[uuid]["string"] = str(points[uuid]["dict"])
		lines[points[uuid]["index"]] = points[uuid]["string"]
 
		break

	return HttpResponse([])

def getresults(request):
	global i

	f = open("tmp-" + str(i),"w")
	f.write(str(request))
	i += 1


	parts = str(request).split(',')
	result = [ 1, 2 , 3]
	for part in parts:
		if "POST" not in part:
			continue
		query = part.strip().split('[')[1].strip().split('\'')[1].strip()
		result = keywordSearch(query)	

		f.write("\n\n"  + str(query) + "\n\n" + str(result))
		break
	f.close()	

	result = str(result)
	result = re.sub('\'','\"',result)
	return HttpResponse([result])
