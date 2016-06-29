file_dir = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling'
inpfile = open(file_dir+'/DatasetsProcessed/ACM_Dataset/input_for_skip_thought.txt','r')
outfile = open(file_dir+'/skip-thoughts/training/test_for_skipthoughts_training.txt','w')

c=0

for curr_line in inpfile:
	curr_line=curr_line.rstrip("\n")
	if c<10:
		outfile.write(curr_line+"\n")
	else:
		break
	c+=1

inpfile.close()
outfile.close()   
