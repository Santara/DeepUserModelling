import numpy as np
import os
import re

file_dir = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/New_Dataset'

inpfile = open(file_dir+'/list_of_identifiers_contents_for_authors.txt', "r")

outfile = open(file_dir+'/list_of_identifiers_contents_for_authors_temp.txt', "w")
iscontent=0

curr_line=''
	
for curr_line in inpfile:
    curr_line.lower()
    curr_line=curr_line.rstrip("\n")
    if curr_line=="<content>":
    	outfile.write(curr_line+'\n')
    	iscontent=1
    elif iscontent==1:
    	curr_line=re.sub(r'\"','\'',curr_line)
    	outfile.write(curr_line+'\n')
    	iscontent=0
    elif curr_line=="</content>":
    	outfile.write(curr_line+'\n')
    else:
    	outfile.write(curr_line+'\n')

inpfile.close()
outfile.close()

