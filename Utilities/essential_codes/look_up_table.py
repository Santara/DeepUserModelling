from collections import defaultdict
import pdb
file_dir = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/ACM_Dataset'
inpfile = open(file_dir + '/adjacency_list.txt', "r")

outfile = open(file_dir + '/infomap_input.txt', "w")
look_up_dict=defaultdict(int)

c=1
for curr_line in inpfile:
	curr_line=curr_line.rstrip("\n")
	a,b=curr_line.split(' ')
	if not look_up_dict[a]:
		look_up_dict[a]=c
		c+=1
	if not look_up_dict[b]:
		look_up_dict[b]=c
		c+=1
	outfile.write(str(look_up_dict[a])+' '+str(look_up_dict[b])+"\n")
inpfile.close()
outfile.close()

