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
import skipthoughts
from time import time
import pickle as pkl

model = skipthoughts.load_model()

data_file = open(file_dir+'new_dataset_of_papers_with_abstract.txt', "r")
author_file = open(file_dir + 'authors_of_interest.txt', "r")
outfile = open(file_dir+'authors_paper_identifiers_vectors.txt','w')

vec_pickle = open(file_dir + '/vector_pickle_temp.pkl', 'wb')

istitle, title1 = 0, ''
isauth = 0
author2,abstract1='',''
author1=[]
author_papers=defaultdict(list)
paper_vectors=defaultdict(list)
isabs,isend=0,0

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
		isauth = 0
	elif isabs == 1:
		if line !='</abstract>':
			abstract1 = line
		isabs = 0
	elif line == '</abstract>':
		isend = 1

	elif line == '<title>':
		istitle = 1
	elif line == '<author>':
		isauth = 1
	elif line == '<abstract>':
		isabs = 1
	elif isend == 1:
		author2=author1[0]
		author2+='$'
		author2 = re.sub('[\s]','_',author2)
		identifier = author2+re.sub('[\s]','_',title1)
		identifier = re.sub(r'\.', '', identifier)
		abstract1 = title1+'$'+abstract1
		abstract1=re.sub(r'\"','\'',abstract1)
		abstract1=abstract1.decode('utf8')
		a=[abstract1]
		vector=skipthoughts.encode(model,a)
		for i in author1:
			if i in unique_authors_set:
				if identifier not in author_papers[i]:
					author_papers[i].append(identifier)
					paper_vectors[i].append(vector)
		author2,title1,abstract1='','',''
		author1=[]
		isend = 0

if isend == 1:
		author2=author1[0]
		author2+='$'
		author2 = re.sub('[\s]','_',author2)
		identifier = author2+re.sub('[\s]','_',title1)
		identifier = re.sub(r'\.', '', identifier)
		abstract1 = title1+'$'+abstract1
		abstract1=re.sub(r'\"','\'',abstract1)
		abstract1=abstract1.decode('utf8')
		a=[abstract1]
		vector=skipthoughts.encode(model,a)
		for i in author1:
			if i in unique_authors_set:
				if identifier not in author_papers[i]:
					author_papers[i].append(identifier)
					paper_vectors[i].append(vector)
		author2,title1,abstract1='','',''
		author1=[]
		isend = 0

pkl.dump({'author_names':paper_vectors.keys(), 'paper_vectors':paper_vectors.values()}, vec_pickle)

for i in author_papers.keys():
	if i!=' ':
		outfile.write('<author>\n'+i+'\n'+'</author>\n'+'<paper>\n')
		for j in author_papers[i]:
			outfile.write(j+'\n')
		outfile.write('</paper>\n')
		outfile.write('<vectors>\n')
		for j in paper_vectors[i]:
			outfile.write(' '.join(list(str(j)[1:-1]))+'\n')
		outfile.write('</vectors>\n\n')
data_file.close()
author_file.close()
outfile.close()
vec_pickle.close()
