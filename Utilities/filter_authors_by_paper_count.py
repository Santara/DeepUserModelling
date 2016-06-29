import os
DATA_PATH = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/New_Dataset'
in_file = open(os.path.join(DATA_PATH, 'author_paper_count_from_new_dataset_sorted.txt'),'r')
out_file = open(os.path.join(DATA_PATH, 'list_of_authors_of_interest_with_paper_counts_sorted.txt'), 'w')
count = 0

MIN_COUNT = 10
MAX_COUNT = 500
for line in in_file:
	count += 1
	if count == 1:
		continue
	else:
		paper_count = line.split(' ')[0]
		if paper_count.isdigit():
			paper_count = int(paper_count)
			if paper_count >= MIN_COUNT and paper_count <= MAX_COUNT:
				out_file.write(line)
	if count % 10000 == 0:
		print "Finished %d " % count

in_file.close()
out_file.close()
