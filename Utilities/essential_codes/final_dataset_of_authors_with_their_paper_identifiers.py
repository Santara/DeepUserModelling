#FIXME: Authors with less than 10 papers entering listS
'''
Take "dataset_of_papers_with_abstract.txt" and ...
"list_of_unique_authors_of_interest_sorted.txt" as input
Make a output file "dataset_with_abstract_for_desired_authors.txt" ...
containing the data of all the desired authors and their papers and abstract.
'''
import re
from collections import defaultdict
file_dir = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/New_Dataset/'



data_file = open(file_dir+'new_dataset_of_papers_with_abstract.txt', "r")
author_file = open(file_dir + 'authors_of_interest.txt', "r")
outfile = open(file_dir+'final_junk.txt','w')

istitle, title1 = 0, ''
isauth = 0
author2=''
author1=[]
author_papers=defaultdict(list)

unique_authors_set = set()
for line in author_file:
	line = line.rstrip('\n')
	unique_authors_set.add(line)
author_file.close()


for line in data_file:
	line = line.rstrip("\n")
	line = line.lower()

	if istitle == 1:
		if line != '</title>':
			title1 = line
		istitle = 0

	elif isauth == 1:
		if line != '</author>':
			author1 = line.split(',')
			for i in author1:
				i=i.strip(' ')
				if len(i) == 0:
					author1.remove(i)
			author2=author1[0]
			author2+='$'
			author2 = re.sub('[\s]','_',author2)
			identifier = author2+re.sub('[\s]','_',title1)
			identifier = re.sub(r'\.', '', identifier)
			for i in author1:
				if i in unique_authors_set:
					if identifier not in author_papers[i]:
						author_papers[i].append(identifier)	
			author2,title1='',''
			author1=[]
		isauth = 0

	elif line == '<title>':
		istitle = 1
	elif line == '<author>':
		isauth = 1

for i in author_papers.keys():
	if i!=' ':
		outfile.write('<author>\n'+i+'\n'+'</author>\n'+'<paper>\n')
		for j in author_papers[i]:
			outfile.write(j+'\n')
		outfile.write('</paper>\n\n')

data_file.close()
author_file.close()
outfile.close()
