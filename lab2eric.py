#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools
lib = []
for line in open('T10I4D100K.dat', 'r'):
    item = line.rstrip()
    temp = []
    for j in item.split(" "):
    	temp.append(int(j))
    lib.append(temp)



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




def getTable2(prev_table,s,k):
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
	check = list(itertools.combinations(list(element),k-1))
	for key in check:
		if key not in prev_table:
			return False
	return True


s = 100
prev_table = getSingletonTable(lib,s)
print(prev_table)
prev_table = getTable2(prev_table,s,2)
print(prev_table)
prev_table = getTable2(prev_table,s,3)
print(prev_table)
prev_table = getTable2(prev_table,s,4)
print(prev_table)



















