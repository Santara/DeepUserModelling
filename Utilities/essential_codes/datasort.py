import numpy as np
import os
from os import listdir 

#cat 2 : acm_output.txt , DBLP-citation-Feb21.txt
#cat 1 : DBLPOnlyCitationOct19, citation-network2.txt, outputacm.txt, DBLP_Citation_2014_May/publications.txt DBLP_Citation_2014_May/domains/*

file_dir = os.path.dirname(os.path.abspath(__file__))

list_dir = [file_dir + '/acm_output.txt' , file_dir+ '/DBLP-citation-Feb21.txt']

output = open(file_dir+'/dataset.txt',"a")

def cat2():
	for i in list_dir:
		print >> output , i
		ct = 0
		datafile = open(i,"r")
		line_num = 0
		for line in datafile:
			if(line.rstrip("\r\n") != ""):
				line_num = line_num + 1
				if(line[0]=='#'):
					line = line.replace(line[0],'')
					if(line[0]=='*'):
						if(ct == 1):
							print >> output, "</abstract>\n"
						print >> output,"<title>"
						line = line.replace(line[0],'')
						print >> output, line.rstrip("\r\n")
						print >> output, "</title>"
						line_num = 1
						ct = 1
					elif (line[0] == '@'):
						print >> output, "<author>"
						line = line.replace(line[0],'')
						print >> output, line.rstrip("\r\n")
						print >> output, "</author>"
						print >> output, "<abstract>"
					elif(line[0] == '!'):
						line = line.replace(line[0],'')
						print >> output, line.rstrip("\r\n")
					elif(line_num>7):
						print >> output, line.rstrip("\r\n")
				else:
					print >> output, line.rstrip("\r\n")
		print >> output, "</abstract>\n"

def cat1(name):
	ct = 0
	datafile = open(name,"r")
	print >> output, name
	line_num = 0
	for line in datafile:
		if(line.rstrip("\r\n") != ""):
			line_num = line_num + 1
			if(line[0]=='#'):
				line = line.replace(line[0],'')
				if(line[0]=='*'):
					if(ct==1):
						print >> output, "</abstract>\n"
					print >> output, "<title>"
					line = line.replace(line[0],'')
					print >> output, line.rstrip("\r\n")
					print >> output, "</title>"
					line_num = 1
					ct = 1
				elif(line[0] == '@'):
					print >> output, "<author>"
					line = line.replace(line[0],'')
					print >> output, line.rstrip("\r\n")
					print >> output, "</author>"
					print >> output, "<abstract>"
				elif(line[0]=='!'):
					line = line.replace(line[0],'')
					line = line.rstrip(" \r\n")
					if(line!=""):
						print >> output,line.rstrip(" \r\n")
				elif(line_num != 3 and line_num!=4 and line_num!=5 and line[0]!='%'):
					line = line.rstrip(" \r\n")
					if(line!=""):
						print >> output,line.rstrip(" \r\n")
			else:
				line = line.rstrip(" \r\n")
				if(line!=""):
					print >> output, line.rstrip(" \r\n")
	print >> output, "</abstract>\n"

file1_cat1 = [file_dir + '/DBLPOnlyCitationOct19', file_dir+'/citation-network2.txt', file_dir+'/outputacm.txt', file_dir+'/DBLP_Citation_2014_May/publications.txt']
for i in file1_cat1:
	cat1(i)
dir2_cat1 = file_dir + '/DBLP_Citation_2014_May/domains'
file2_cat1 = listdir(dir2_cat1)
for i in file2_cat1:
	cat1(dir2_cat1+'/'+i)
	print i
cat2()
print "success"
