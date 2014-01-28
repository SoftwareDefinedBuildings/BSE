# Create your views here.

from django.template import Context, loader
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect, HttpResponseBadRequest, Http404
from django.contrib.admin import site as adminsite
from search import * 
import re
i = 0
lines = open("search/MetadataDump_flattened").readlines()
points = [ 
def search(request):
    t = loader.get_template('search2.html')
    c = Context({})
    return HttpResponse(t.render(c))

def getresultsStatus(request):
	global i
	global lines

	#f = open("temp-" + str(i),"w")
	#f.write(str(request))
	i += 1


	parts = str(request).split(',')
	result = [ ]
	for part in parts:
		if "POST" not in part:
			continue
		#f.write(" Number of lines in read file : " + str(len(lines)))
		query = part.strip().split('\'')[1].strip()
		result = parse_query(lines,query,1000)	

		if len(result) == 0:
			result = [ {"Path" : "No results" } ]
		#f.write("\n\n"  + str(query) + "\n\n" + str(result))
		break
	#f.close()	

	result = str(result)
	result = re.sub('\'','\"',result)
	return HttpResponse([result])


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