import os
import numpy as np 
import matplotlib.pyplot as plt 
DATA_PATH = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/New_Dataset'
in_file = open(os.path.join(DATA_PATH, 'paper_counts.txt'),'r')
# out_file = open(os.path.join(DATA_PATH, 'authors_and_paper-counts.txt'),'w')

count = 0
arr = []
for curr_line in in_file:
	# arr.append(np.log10(float(curr_line.rstrip('\n'))))
	arr.append(int(curr_line.rstrip('\n')))
plt.hist(arr,bins=1000,log=True)
plt.xlabel('log of paper-count')
plt.ylabel('Number of authors in a given bin')
plt.show()
