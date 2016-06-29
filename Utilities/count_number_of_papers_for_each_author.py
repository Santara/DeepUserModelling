import os
import matplotlib.pyplot as plt 
DATA_PATH = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/'
in_file = open(os.path.join(DATA_PATH, 'list_of_paper_counts.txt'),'r')
# out_file = open(os.path.join(DATA_PATH, 'authors_and_paper-counts.txt'),'w')

count = 0
arr = []
for curr_line in in_file:
	arr.append(int(curr_line.rstrip('\n')))
plt.hist(arr,bins=1000)
plt.show()