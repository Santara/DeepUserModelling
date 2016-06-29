import pdb
f = open('../DatasetsProcessed/NewData/acm.txt','r')
keyword = '#index'
count = 0
# pdb.set_trace()
for line in f:	
	if keyword in line:
		count += 1
print "count = %d " % count
f.close()
