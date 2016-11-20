#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
lib = []
#for line in open('T10I4D100K.dat', 'r'):
#    item = line.rstrip()
#    temp = []
#    for j in item.split(" "):
#    	temp.append(int(j))
#    lib.append(temp)



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
	print("HEJ")
	temp1 = set(itertools.combinations(itemList,k))
	valid_permutations = set([x for x in temp1 if checkPerm(x,prev_table,k)])
	print(valid_permutations)
	print("TA")
	itemList = set(itemList)
	print("yo")
	counter=0
	for bag in lib:
		current = list(itemList.intersection(bag))
		current.sort()
		counter+=1
		if counter%1000==0:
			print(counter)
		current_permutations=list(itertools.combinations(current,k))
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




def getTable2(prev_table,s,k,lib):
	table = {}
	itemList = set(getItemList(prev_table.keys()))
	counter = 0
	for bag in lib:
		current = list(itemList.intersection(bag))
		current.sort()
		counter+=1
		if counter%1000==0:
			print(counter)
		current_permutations=(list(itertools.combinations(current,k)))
		for key in current_permutations:
			if checkPerm(key,prev_table,k):
				if key in table:
					table[key]+=1
				else:
					table[key]=1
	for key in table.keys():
		if table[key]<s:
			del table[key]
	return table





def checkPerm(element,prev_table,k):
	if len(element)<k:
		return False
	check = list(itertools.combinations(list(element),k-1))
	for key in check:
		if key not in prev_table:
			return False
	return True

def getConfidence(tables,left,right):
	l = list(set(left)|set(right))
	l.sort()
	l = tuple(l)
	r = left
	right = tuple(right)
	conf = float(tables[len(l)][l])/float(tables[len(r)][r])
	return conf


def getAssosciation(tables,k,c,association):
	counter = 1
	while counter<k:
		for key in tables[k]:
			items = list(key)
			left = set(itertools.combinations(list(items),counter))
			items = set(items)
			for tup in left:
				right = items.symmetric_difference(tup)
				conf = getConfidence(tables,tup,right)
				if conf>c:
					association[tuple([tuple(tup),tuple(right)])]=conf
		counter+=1


def generateAssociations(tables,c):
	association = {}
	length = len(tables)
	for k in range(2,length):
		getAssosciation(tables,k,c,association)

	return association

# (B,C) & \rightarrow  & (A) & 0.92
def convertTupleToString(tup):
	string = "("
	for t in tup:
		string+=str(t)+","
	string = string[0:-1]+")"
	return string

def getLatex(association):
	string = ""
	temp = association.keys()
	temp.sort()
	for key in temp:
		print(key)

string="\\\\"
print(string)
print(convertTupleToString(tuple([1])))


def printAssociations(association):
	for key in association:
		left = key[0]
		right = key[1]
		conf = association[key]
		print(str(left)+"\t->\t"+str(right)+"\tCONF: "+str(conf))


def getTables(lib,support,confidence):
	tables = [(1,)]
	prev_table = getSingletonTable(lib,support)
	tables.append(prev_table)
	k=2
	while len(prev_table)>0:
		prev_table = getTable2(prev_table,support,k,lib)
		if len(prev_table)>0:
			print(prev_table)
			tables.append(prev_table)
		k+=1
	return tables

def main():
	support = 1000
	confidence = 0.5
	lib = []
	for line in open('T10I4D100K.dat', 'r'):
	    item = line.rstrip()
	    temp = []
	    for j in item.split(" "):
	    	temp.append(int(j))
	    lib.append(temp)
	tables = getTables(lib,support,confidence)
	associations = generateAssociations(tables,confidence)
	printAssociations(associations)
	getLatex(associations)
	for i in tables:
		print(len(i))
main()