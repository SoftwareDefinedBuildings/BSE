import os
import sys
import commands
import ast

def keywordSearch(string):
		words = string.split(' ')
		query = "grep -i " + words[0] + " search/MetadataDump"

		for word in words[1:]:
			word = word.strip()
			if word == '':
				continue
			query = query + " | grep -i " + word

		(status, output) = commands.getstatusoutput(query)

		lines = output.split('\n')
		results = []
		for line in lines:
			point = ast.literal_eval(line.strip())
			results.append(point)

		return results

