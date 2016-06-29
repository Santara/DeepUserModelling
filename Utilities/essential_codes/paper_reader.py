import numpy as np
import os
import re
import pdb

def read_a_paper(inpfile):

	isidentifier,iscontent=0,0
	identifier,content='',''
	
	curr_line=''
	while curr_line == '':
		curr_line=inpfile.readline()
		curr_line=curr_line.rstrip("\n")

	while curr_line!="</content>":
	    curr_line.lower()
	    if curr_line == "<identifier>":
        	isidentifier = 1
	    elif curr_line == "<content>":
    		iscontent = 1
	    elif isidentifier == 1:
	        identifier = curr_line
	        isidentifier = 0
	    elif iscontent == 1:
	        content = curr_line
	        iscontent = 0
	    curr_line=inpfile.readline()
	    curr_line=curr_line.rstrip("\n")
	    while curr_line == '':
			curr_line=inpfile.readline()
			curr_line=curr_line.rstrip("\n")
	
	return identifier, content

if __name__ == '__main__':
	DATA_DIR = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed'
	f_input = open(os.path.join(DATA_DIR, 'tiny_data.txt'), 'r')
	for i in range(10):
		# pdb.set_trace()
		identifier, content = read_a_paper(f_input)
		print "Paper %d" % i , '\n' , identifier , '\n', content
	f_input.close()

# def read_a_full_paper(inpfile):
