file_dir = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed'
inpfile = open(file_dir+'/ACM_Dataset/dataset_new.txt','r')
outfile = open(file_dir+'/ACM_Dataset/input_for_skip_thought.txt','w')
a=0
for curr_line in inpfile:
	curr_line=curr_line.rstrip("\n")
	if curr_line=="<abstract>":
		a=1
	elif curr_line!="</abstract>" and a==1:
		for line in curr_line.split("."):
			outfile.write(line+"\n")
		a=0

inpfile.close()
outfile.close()	


