import numpy as np
import os
import re
from collections import defaultdict
import pdb
import skipthoughts
from time import time
import pickle as pkl
import scipy.io as io

model = skipthoughts.load_model()

file_dir = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/New_Dataset'
checkfile = open(file_dir + '/list_of_three_authors_and_their_papers.txt', "r")

outfile = open(file_dir + '/list_of_three_authors_with_their_paper_vectors.txt', "w")
#vec_pickle = open(file_dir + '/vector_pickle.pkl', 'wb')

curr_line, line = '', ''
isauthor, ispaper = 0, 0
a = 0

isabstract = 0
abstract = defaultdict(list)
identifier = defaultdict(list)
#pdb.set_trace()
for curr_line in checkfile:
	curr_line = curr_line.rstrip("\n")
	curr_line = curr_line.lower()

	if curr_line == "<paper>":
		ispaper = 1
		inpfile = open(file_dir + '/list_of_identifiers_contents_for_authors_temp.txt', "r")
	elif curr_line == "<author>":
		isauthor = 1
	elif isauthor == 1:
		author = curr_line
		
		isauthor = 0

	elif curr_line == "</paper>":
		#pdb.set_trace()
		ispaper = 0
		author = ''
		inpfile.close()
	elif ispaper == 1:

		for line in inpfile:
			line = line.rstrip("\n")
			line = line.lower()

			if curr_line == line:
				identifier[author].append(curr_line)
				a = 1
				# print author
				continue
			elif a == 1 and line == "<content>":
				isabstract = 1
			elif a == 1 and isabstract == 1:
				abstract[author].append(line.decode('utf8'))
				a = 0
				isabstract = 0
				break

authors = abstract.keys()
vectors_of_papers_for_diff_authors = []
for i in abstract.keys():
	t = time()
	outfile.write("<author>" + "\n")
	outfile.write(i + "\n")
	#print i
	outfile.write("</author>" + "\n")
	outfile.write("<paper_id>" + "\n")
	for j in identifier[i]:
		outfile.write(j + "\n")
	outfile.write("</paper_id>" + "\n")
	outfile.write("<paper_vector>" + "\n")
	# for k in abstract[i]:
	# 	print k
	# 	abs_in_list = [k]
	vecs = skipthoughts.encode(model,abstract[i])
	vectors_of_papers_for_diff_authors.append(vecs)

	for vec in vecs:
		outfile.write(" ".join(str(vec)[1:-1])+'\n')

	outfile.write("</paper_vector>" + "\n\n")
	#print "Time taken for author: ", i, time()-t

dict_temp = {'author_names':authors, 'paper_vectors':vectors_of_papers_for_diff_authors}
#pkl.dump({'author_names':authors, 'paper_vectors':vectors_of_papers_for_diff_authors}, vec_pickle)
io.savemat('vectors_three_authors.mat',dict_temp)
checkfile.close()
outfile.close()
#vec_pickle.close()
