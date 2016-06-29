file_dir = "/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/New_Dataset/"

in_file = open(file_dir+"dataset_of_desired_authors_with_their_paper_identifiers.txt",'r')
out_file = open(file_dir+"papers_of_interest.txt",'w')

count = 0

is_auth,is_paper,isend=0,0,0
author1=''

papers_set=set()

for line in in_file:
	line = line.rstrip('\n')
	if line == "<paper>":
		is_paper = 1
	elif is_paper == 1 and line!="</paper>":
		if line not in papers_set:
			papers_set.add(line)
	elif line == "</paper>":
		is_paper = 0
for i in list(papers_set):
	out_file.write(i+'\n')
in_file.close()
out_file.close()