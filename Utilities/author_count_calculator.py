import os

DATA_PATH = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/New_Dataset/'
in_file = open(os.path.join(DATA_PATH, 'new_dataset_of_papers_with_abstract.txt'),'r')
out_file = open(os.path.join(DATA_PATH, 'list_of_authors.txt'),'w')

count = 0
is_author = 0
for curr_line in in_file:
	curr_line = curr_line.rstrip('\n')
	if is_author == 1:
		list_of_authors = curr_line.split(',')
		for author in list_of_authors:
			out_file.write(author+'\n')
		is_author = 0
	elif curr_line == "<author>":
		is_author = 1

	if count % 1000000 == 0:
		print "Processed %d lines" % count

	count += 1

in_file.close()
out_file.close()
