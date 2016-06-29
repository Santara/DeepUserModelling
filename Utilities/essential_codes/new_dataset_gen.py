import pdb
file_dir = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed'
inpfile = open(file_dir+'/NewData/acm.txt','r')
outfile = open(file_dir+'/ACM_Dataset/dataset_new.txt','w')

temp,temp1 = 0,0

for line in inpfile:
	line = line.rstrip('\n')
	line = line.lower()
	line = line.strip(' ')
	if len(line) > 2:
		line = line[1:]
		if line[0] == '*':
			outfile.write('<title>\n'+line[1:]+'\n</title>\n')
		elif line[0] == '@':
			outfile.write('<author>\n'+line[1:]+'\n</author>\n')
		elif line[0:5]=='index':
			outfile.write('<index>\n'+line[5:]+'\n</index>\n'+'<citations>\n')
			temp = 1
		elif temp == 1 and line[0] == '%':
			outfile.write(line[1:]+'\n')
		elif temp == 1 and line[0] != '%' and line[0] =='!':
			outfile.write('</citations>\n'+'<abstract>\n'+line[1:]+'\n'+'</abstract>\n\n')
			temp = 0
	elif temp == 1 :
		outfile.write('</citations>\n'+'<abstract>\n'+'</abstract>\n\n')
		temp = 0
inpfile.close()
outfile.close()