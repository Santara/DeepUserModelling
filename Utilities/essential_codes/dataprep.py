import numpy as np
import os
import re

file_dir = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/New_Dataset'

inpfile = open(file_dir+'/new_dataset_of_papers_with_abstract.txt', "r")

transfile = open(file_dir+'/list_of_identifiers_contents_for_authors.txt', "w")

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
		abstract1=''
		isend = 1
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
		transfile.write('<identifier>\n')
		l=author1.split(',')
		author1=l[0]
		author1+='$'
		author1 = re.sub(r'\.', '', author1)
		transfile.write(re.sub('[\s]','_',author1))
		b = re.sub('[\s]','_',title1)
		b = re.sub(r'\.', '', b)
		transfile.write(b)
		transfile.write('\n</identifier>\n')
		transfile.write('<content>\n')
		transfile.write(title1)
		b+= '$'
		transfile.write(abstract1)
		transfile.write('\n</content>\n\n')
		title1,author1,abstract1='','',''
		isend = 0
if isend == 1:
	transfile.write('<identifier>\n')
	l=author1.split(',')
	author1=l[0]
	author1+='$'
	author1 = re.sub(r'\.', '', author1)
	transfile.write(re.sub('[\s]','_',author1))
	b = re.sub('[\s]','_',title1)
	b = re.sub(r'\.', '', b)
	transfile.write(b)
	transfile.write('\n</identifier>\n')
	transfile.write('<content>\n')
	transfile.write(title1)
	b+= '$'
	transfile.write(abstract1)
	transfile.write('\n</content>\n\n')
	title1,author1,abstract1='','',''
	isend = 0
inpfile.close()
print >> transfile
transfile.close()
