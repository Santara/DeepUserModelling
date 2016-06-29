filedir = "/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/New_Dataset/"

infile=open(filedir+'desired_authors_dataset_junk.txt','r')
outfile=open(filedir+'junk.txt','w')
isauth=0
authors=set()

for i in infile:
	i=i.rstrip('\n')
	if i =="<author>":
		isauth = 1
	elif isauth == 1:
		k=i.split(',')
		for j in k:
			if j not in authors:
				authors.add(j)
		isauth =0 
p=list(authors)
for i in p:
	outfile.write(i+'\n')
infile.close()
outfile.close()