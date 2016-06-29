'''
Take "dataset_of_papers_with_abstract.txt" and ...
"list_of_unique_authors_of_interest_sorted.txt" as input
Make a output file "dataset_with_abstract_for_desired_authors.txt" ...
containing the data of all the desired authors and their papers and abstract.
'''

file_dir = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/'

data_file = open(file_dir+'/dataset_of_papers_with_abstract.txt', "r")

outfile = open(file_dir+'/New_Dataset/new_dataset_of_papers_with_abstract.txt','w')

istitle, title1 = 0, ''
isabs, abstract1 = 0, ''
isauth, author1 = 0, ''
isend = 0

#unique_authors_set = set()
#for line in author_file:
#	line = line.rstrip('\r\n')
#	unique_authors_set.add(line)
#author_file.close()

titles_set=set()

flag = 0
flag1 = 0
for line in data_file:
	line = line.rstrip("\r\n")
	line = line.lower()
	
	if flag == 1 and line!="<title>":
		continue
	elif flag1 == 1 and line!="<title>":
		continue

	elif istitle == 1:
		if line != '</title>':
			line = re.sub(r'\.', '', line)
			if line not in titles_set:
				titles_set.add(title1)
				title1 = line
			else:
				flag = 1
				istitle = 0
				continue
		istitle = 0

	elif isabs ==1 and line == '</abstract>':
		isabs = 0

	elif isabs == 1 and line != '</abstract>':
		abstract1 = line
		isabs = 0

	elif isabs == 0 and line == '</abstract>':
		isend = 1

	elif isauth == 1:
		if line != '</author>':
			author1 = line.split(',')
			for i in author1:
				i=i.strip(' ')
				if len(i) == 0:
					author1.remove(i)
			if len(author1)==0:
				flag1 = 1
				isauth = 0
				continue

		isauth = 0

	elif line == '<title>':
		flag = 0
		flag1 = 0
		istitle = 1

	elif line == '<abstract>':
		isabs = 1

	elif line == '<author>':
		isauth = 1

	elif isend == 1:
		outfile.write('<title>' + '\n' + title1 + '\n' + '</title>' + '\n')
		outfile.write('<author>' + '\n' + ','.join(author1) + '\n' + '</author>' + '\n')
		outfile.write('<abstract>' + '\n' + abstract1 + '\n' + '</abstract>' + '\n\n')
		title1, author1, abstract1 = '', '', ''
		isend = 0

if isend == 1:
	outfile.write('<title>' + '\n' + title1 + '\n' + '</title>' + '\n')
	outfile.write('<author>' + '\n' + ','.join(author1) + '\n' + '</author>' + '\n')
	outfile.write('<abstract>' + '\n' + abstract1 + '\n' + '</abstract>' + '\n\n')
	title1, author1, abstract1 = '', '', ''
	isend = 0

author_file.close()
data_file.close()
#print >> outfile
outfile.close()