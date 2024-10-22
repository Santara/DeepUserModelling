import numpy as np
import matplotlib.pyplot as plt 
file_dir = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/ACM_Dataset/infomap_output'
inpfile = open(file_dir + '/populations_dump.txt', "r")

#outfile = open(file_dir + '/list_of_three_authors_with_their_paper_vectors.txt', "w")


arr = []

for curr_line in inpfile:
	curr_line = curr_line.rstrip("\n")
	arr.append(np.float(curr_line))

a,b,c=plt.hist(arr,bins = 1000,log=True)
plt.xlabel('Population of communities')
plt.ylabel('Frequencies')
plt.show()
