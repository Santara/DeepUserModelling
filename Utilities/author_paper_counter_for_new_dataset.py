filedir = "/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/New_Dataset/"

in_file = open(filedir+"new_dataset_of_papers_with_abstract.txt",'r')
out_file = open(filedir+"author_paper_count_from_new_dataset.txt",'w')

from collections import defaultdict
paper_counts=defaultdict(int)
isauth = 0
author1 = ''

for line in in_file:
	line = line.rstrip('\n')
	if line == "<author>":
		isauth = 1
	elif isauth == 1:
		author1 = line.split(",")
		for i in author1:
			paper_counts[i]+=1
		isauth = 0
for i in paper_counts.keys():
	out_file.write(str(paper_counts[i])+' '+i+'\n')
in_file.close()
out_file.close()