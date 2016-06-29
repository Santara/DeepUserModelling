import os

DATA_PATH = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/'
in_file = open(os.path.join(DATA_PATH, 'dataset.txt'),'r')

isabs,abstract_count = 0,0

for line in in_file:
	line = line.rstrip('\n')
	if isabs == 1 and line == "</abstract>":
		isabs = 0
	elif isabs == 1 and line != "</abstract>":
		abstract_count+=1
		isabs = 0
	elif line == "<abstract>":
		isabs = 1
print abstract_count