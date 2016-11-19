import itertools
lib = []
lib2 = []
for line in open('T10I4D100K.dat', 'r'):
    item = line.rstrip()
    temp = []
    temp2 = set([])
    for j in item.split(" "):
    	temp.append(int(j))
    	temp2.add(int(j))
    lib.append(temp)
    lib2.append(temp2)

count = 0
for bag in lib2:
	if 39 in bag and 704 in bag and 825 in bag:
		count+=1

print(count)





def getSingletonTable(lib,s):
	table = {}
	for bag in lib:
		for val in bag:
			key = tuple([val])
			if key in table:
				table[key]+=1
			else:
				table[key]=1
	for key in table.keys():
		if table[key]<s:
			del table[key]
	return table


def getItemList(prev_table_keyset):
	itemlist = set([])
	for key in prev_table_keyset:
		for val in key:
			itemlist.add(val)
	return list(itemlist)


def getTable(prev_table,s,k):
	table = {}
	itemList = getItemList(prev_table.keys())
	itemList.sort()
	valid_permutations = set(itertools.combinations(itemList,k))
	for bag in lib:
		current_permutations = list(itertools.combinations(bag,k))
		for key in current_permutations:
			if key in valid_permutations:
				if key in table:
					table[key]+=1
				else:
					table[key]=1

	for key in table.keys():
		if table[key]<s:
			del table[key]
	return table

s = 1000
prev_table = getSingletonTable(lib,s)
print(len(prev_table))
prev_table = getTable(prev_table,s,2)
print(len(prev_table))
prev_table = getTable(prev_table,s,3)
print(len(prev_table))


