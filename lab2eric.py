

lib = []
corpus = [[1,2,3],[2,3],[2,3,4],[1,5],[1,2,5]]
#for line in open('T10I4D100K.dat', 'r'):
#    item = line.rstrip()
#    temp = []
#    for j in item.split(" "):
#    	temp.append(int(j))
#    	corpus.add(int(j))
#    lib.append(temp)




def getKey(l):
	l.sort()
	return tuple(l)

def getSingleTonTable(corpus,s):
	table = {}
	for bag in corpus:
		for j in bag:
			temp = [j]
			key = getKey(temp)
			if key in table:
				table[key]+=1
			else:
				table[key]=1

	for key in table.keys():
		if table[key]<s:
			del table[key]
	return table

def getTable(corpus,previous,n):
	for bag in corpus:
		


print(getSingleTonTable(corpus,2))







