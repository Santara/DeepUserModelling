#FIXME: Authors with less than 10 papers entering listS

import numpy as np
import os
import re
from collections import defaultdict
author_papers = defaultdict(list)

file_dir = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/New_Dataset'

inpfile = open(file_dir+'/dataset_of_desired_authors_with_abstract.txt', "r")
outfile = open(file_dir+'/temp.txt','w')

#transfile = open(file_dir+'/list_of_paper_identifiers_and_their_contents.txt', "w")
count = 0
istitle,title1 = 0,''
isabs,abstract1 = 0,''
isauth,author1 = 0,''
isend = 0
#pdb.set_trace()
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
			k = author1.split(',')
			for i in k:
				i=i.strip(" ")
				if len(i) == 0:
					k.remove(i)
			author1 = ','.join(k)
		isauth = 0

	elif line == "<title>":
		istitle = 1

	elif line == "<abstract>":
		isabs = 1
	elif line == "<author>":
		isauth = 1
		
	
	elif isend == 1:
		count+=1
		l=author1.split(',')
		author1=l[0]
		author1+='$'
		author1 = re.sub('[\s]','_',author1)
		identifier = author1+re.sub('[\s]','_',title1)
		identifier = re.sub(r'\.', '', identifier)
		if count % 50000 ==0:
			print identifier
		for i in k:
			if identifier not in author_papers[i] and i!=' ':
				author_papers[i].append(identifier)
		title1,author1,abstract1='','',''
		isend = 0
if isend == 1:
	l=author1.split(',')
	author1=l[0]
	author1+='$'
	author1 = re.sub('[\s]','_',author1)
	identifier = author1+re.sub('[\s]','_',title1)
	identifier = re.sub(r'\.', '', identifier)
	for i in k:
		if identifier not in author_papers[i] and i!=' ':
			author_papers[i].append(identifier)
	title1,author1,abstract1='','',''
	isend = 0

for i in author_papers.keys():
	if i!=' ':
		outfile.write('<author>\n'+i+'\n'+'</author>\n'+'<paper>\n')
		for j in author_papers[i]:
			outfile.write(j+'\n')
		outfile.write('</paper>\n\n')
inpfile.close()
outfile.close()