import os
import sys
import commands
import ast

def keywordSearch(in_lines,string):
		words = string.split(' ')

		out_lines = []
		for line in in_lines:
			line = line.strip()
			flag = 0
			for word in words:
				word = word.strip()
				if word == '':
					continue
				if word.upper() not in line.upper():
					flag = 1
					break

			if flag == 0:
				out_lines.append(line)
	

		results = []
		for line in out_lines:
			point = ast.literal_eval(line.strip())
			results.append(point)

		return results

