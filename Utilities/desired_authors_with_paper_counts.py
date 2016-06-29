file_dir = "/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/New_Dataset/"

in_file = open(file_dir+"dataset_of_desired_authors_with_their_paper_identifiers.txt",'r')
out_file = open(file_dir+"new_authors_with_paper_count.txt",'w')

count = 0

is_auth,is_paper,isend=0,0,0
author1=''

for line in in_file:
	line = line.rstrip('\n')
	if line == "<author>":
		is_auth = 1
	elif line == "<paper>":
		is_paper = 1
	elif is_auth == 1:
		author1 = line
		is_auth = 0
	elif is_paper == 1 and line!="</paper>":
		count += 1
	elif line == "</paper>":
		count = 0
		isend = 1
		is_paper = 0
	elif isend == 1:
		out_file.write(count+' '+author1+'\n')
if isend == 1:
	out_file.write(count+' '+author1+'\n')
in_file.close()
out_file.close()