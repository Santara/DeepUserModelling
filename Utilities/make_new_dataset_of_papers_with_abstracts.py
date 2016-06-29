# read a paper
# if abstract is present
# write down the paper in new dataset file
import numpy as np
import os
import re

file_dir = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/'

inpfile = open(file_dir+'/dataset.txt', "r")

transfile = open(file_dir+'/dataset_of_papers_with_abstract.txt', "w")

istitle,title1 = 0,''
isabs,abstract1 = 0,''
isauth,author1 = 0,''
isend = 0

for line in inpfile:
	line = line.rstrip("\r\n")
	line = line.lower()
	if istitle == 1:
		if line!="</title>":
			title1 = line
			#print >> transfile, "<identifier>"
			#print >> transfile, re.sub('[\s]+', '_', line),
		istitle = 0
	elif isabs == 1 and line == "</abstract>":
		isabs = 0
	elif isabs == 1 and line != "</abstract>":
		abstract1 = line
		isabs = 0
		#	print >> transfile, re.sub('[^A-Za-z0-9]+', ' ', line),
	elif isabs == 0 and line == "</abstract>":
		isend = 1
	elif isauth == 1:
		if line!="</author>":
			author1 = line
		isauth = 0

	elif line == "<title>":
		istitle = 1

	elif line == "<abstract>":
		isabs = 1
	elif line == "<author>":
		isauth = 1
		
	
	elif isend == 1:
		transfile.write('<title>\n'+title1+'\n'+'</title>'+'\n')
		transfile.write('<author>'+'\n'+author1+'\n'+'</author>'+'\n')
		transfile.write('<abstract>'+'\n'+abstract1+'\n'+'</abstract>'+'\n\n')
		title1,author1,abstract1='','',''
		isend = 0
if isend == 1:
	transfile.write('<title>\n'+title1+'\n'+'</title>'+'\n')
	transfile.write('<author>'+'\n'+author1+'\n'+'</author>'+'\n')
	transfile.write('<abstract>'+'\n'+abstract1+'\n'+'</abstract>'+'\n\n')
	title1,author1,abstract1='','',''
	isend = 0
inpfile.close()
print >> transfile
transfile.close()
