import os
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as pl
import re
file_dir = os.path.dirname(os.path.abspath(__file__))
inp_file = open(file_dir+'/data_prepared_for_skipthoughts.txt','r')
is_identifier = 0
author_list=set()
number_of_papers=defaultdict(int)

for curr_line in inp_file:
	curr_line=curr_line.rstrip("\n")
	if is_identifier == 1:
		temp = curr_line.split('$')
		number_of_papers[temp[0]]+=1
		if temp[0] in author_list:
			is_identifier = 0
			continue
		else:
			author_list.add(temp[0])
			is_identifier = 0
	elif curr_line == "<identifier>":
		is_identifier = 1


for i in number_of_papers.keys():
	j = re.sub('[^A-Za-z0-9]','',i)
	number_of_papers[j] = number_of_papers[i]
	del number_of_papers[i]

print number_of_papers
print max(number_of_papers.values())
'''
X = np.arange(len(number_of_papers))
pl.bar(X, number_of_papers.values(), align='center', width=0.2)
pl.xticks(X, number_of_papers.keys())
pl.xticks(rotation=10)
ymax = max(number_of_papers.values()) + 1
pl.ylim(0, ymax)
pl.show()
inp_file.close()
'''