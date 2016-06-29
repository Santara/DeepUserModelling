import numpy as np
import os
import re

file_dir = os.path.dirname(os.path.abspath(__file__))

inpfile = open(file_dir+'/dataset.txt', "r")

transfile = open(file_dir+'/inp', "w")

istitle=0
isabs=0

for line in inpfile:
	line = line.rstrip("\r\n")
	line = line.lower()
	# print line
	if istitle == 1:
		print >> transfile, re.sub('[^A-Za-z0-9]+', ' ', line),
		istitle = 0
	elif isabs == 1:
		if line != "</abstract>":
			print >> transfile, re.sub('[^A-Za-z0-9]+', ' ', line),
		isabs = 0
	elif line == "<title>":
		istitle = 1
	elif line == "<abstract>":
		isabs = 1
inpfile.close()
print >> transfile
transfile.close()
