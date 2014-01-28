import os
import sys
import commands
import ast

def keywordSearch(in_lines,string,maxresults):
		string = string.upper()
		words = string.split(' ')

		out_lines = []
	
		count = 0	
		for line in in_lines:
			line = line.strip()
			flag = 0
			for word in words:
				word = word.strip()
				if word == '':
					continue
				if word not in line.upper():
					flag = 1
					break
			if flag == 0:
				pathFlag = 0
				point = ast.literal_eval(line.strip())
				for word in words:
					if word.strip() == '':
						continue
					if word.strip().upper() not in point["uuid"].upper() and word.strip().upper() not in point["Path"].upper():
						pathFlag = 1
						break

				if pathFlag == 1:
					out_lines.append(point)
					count += 1

			if count == maxresults:
				break

		return out_lines

		results = []
		for line in out_lines:
			point = ast.literal_eval(line.strip())
			results.append(point)

		return results

	
