file_dir = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/'

inpfile = open(file_dir+'/dataset_of_authors_with_their_papers.txt', "r")
outfile = open(file_dir+'/temp.txt','w')

a = 0
for line in inpfile:
	line =line.rstrip('\r\n')
	if a == 0:
		while line != '</paper>':
			continue
		a = 1

	outfile.write(line + '\n')

inpfile.close()
outfile.close()