

lib = []

for line in open('T10I4D100K.dat', 'r'):
    item = line.rstrip()
    temp = []
    for j in item.split(" "):
    	temp.append(int(j))
    lib.append(temp)
#lib =  [[1,2,3],[2,3],[2,3,4],[1,5],[1,2,5]]
def getCorpus(lib):
	corpus = set([])
	for bag in lib:
		for value in bag:
			corpus.add(value)
	corpus = list(corpus)
	corpus.sort()
	return corpus




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

bag = [1,2,3,4]


def getSubsets(bigSet,k,idx,subset,solution):
	if len(subset)==k:
		subset.sort()
		solution.append(tuple(subset))
		return

	if idx==len(bigSet):
		return

	x = bigSet[idx]
	subset.append(x)
	getSubsets(bigSet, k, idx+1, subset, solution)
	subset.remove(x)
	getSubsets(bigSet, k, idx+1, subset, solution)


def getTable(k,lib,s):
	table = {}
	for bag in lib:
		perms = []
		getSubsets(bag,k,0,[],perms)
		for key in perms:
			if key in table:
				table[key]+=1
			else:
				table[key]=1

	for key in table.keys():
		if table[key]<s:
			del table[key]
	return table


def convertToList(tuplelist):
	for key in hej:
		for val in key:
			temp.append(val)


def getTableAboveOne(k,lib,s,prev_table):
	table = {}
	valid_perms = []
	bigSet = prev_table.keys()
	temp = []
	for key in bigSet:
		for val in key:
			temp.append(val)
	getSubsets(temp,k,0,[],valid_perms)
	valid_perms = set(valid_perms)

	for bag in lib:
		current_perms = []
		getSubsets(bag,k,0,[],current_perms)
		for perm in current_perms:
			if perm in valid_perms:
				if perm in table:
					table[perm]+=1
				else:
					table[perm]=1

	for key in table.keys():
		if table[key]<s:
			del table[key]
	return table



s = 500
prev_table = getTable(1,lib,s)

print(prev_table)
print("\n\n")


prev_table = getTableAboveOne(2,lib,s,prev_table)
print(prev_table)
print("\n\n")
prev_table = getTableAboveOne(3,lib,s,prev_table)
print(prev_table)

