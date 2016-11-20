import math
import itertools

def parseData ():
	data = {}
	baskets = []
	for line in open ('T10I4D100K.dat', 'r'):
		temp = line.rstrip().split(" ")
		basket = []
		for item in temp:
			item = int(item)
			basket.append(item)
			key = tuple ([item])
			if key in data:
				data[key] += 1
			else: 
				data[key] = 1

		baskets.append(basket)
			
	s = int (0.01 * len (baskets))

	for k in data.keys():
		if data[k] < s:
			del data[k]

	print ""
	print "Support threshold (1% of baskets-length): " + str(s)

	return data, baskets, s

"""  This function retrieves a higher order Lset from the lower order.
	Will retrieve a narrowed L1 from singeton combinations of prevLset tuples
	From this it makes candidates of items in each basket that are in narrowed L1.
	Each k-tuple candidates will be verified if the subset of k-1-tuples from the 
	candidate exists in L_(k-1) (i.e "ABC" will only be verified if "AB, AC, BC" exist) 
	The verified candidates will then be counted and pruned """
def getLset (prevLset, baskets, s, k):
	newLset = {}
	L1 = getNarrowedL1 (prevLset.keys())
	
	for basket in baskets:
		#Get all items from basket that are in L1
		valid_basket = list(L1.intersection (basket))
		valid_basket.sort()
		# Get all candidates from the current basket
		candidates = list(itertools.combinations (valid_basket, k))	
		for key in candidates:
			# Check if all k-1-tuples of the candidate exist in L_(k-1)
			if checkCandidate (key, prevLset, k):
				if key in newLset:
					newLset[key] += 1
				else:
					newLset[key] = 1

	# Prune the valid candidates
	for key in newLset.keys():
		if newLset[key] < s:
			del newLset[key]

	return newLset

			
# Returns a set of unique singletons in L_k 	
def getNarrowedL1 (prevLset):
	items = set([])
	for key in prevLset:
		for val in key:
			items.add(val)

	return items

# Checks if all combinations (k-1-tuples) of a k-tuple exist i L_(k-1)
def checkCandidate (element, prevLset, k):
	combinations = itertools.combinations (list(element), k-1)
	for key in combinations:
		if key not in prevLset:
			return False
	return True



def AprioriAlgo ():
	# Retrieve L1, the baskets and the support threshold
	L_1, baskets, s = parseData ()

	resultSet = [(1,)]
	Lset = L_1
	k = 2
	# Fetch higher order pruned Lsets until	there exists no more
	while (len(Lset) > 0):
		resultSet.append (Lset)
		Lset = getLset (Lset, baskets, s, k)
		k += 1

	return resultSet

#---  END OF ASSIGNEMENT 1 -- NOW LETS FIND ASSOCIATION RULES ----

def getConfidence (itemSets, s1, s2):
	union = list (set(s1) | set(s2))
	union.sort()
	union = tuple(union)
	conf = float(itemSets[len(union)][union]) / itemSets[len(s1)][s1]

	return conf

def getAssociation (itemSets, k, c, associations):
	counter = 1
	while counter < k:
		for key in itemSets[k]:
			items = list(key)
			left = set(itertools.combinations(list(items), counter))
			items = set(items)
			for _tuple in left:
				right = items.symmetric_difference(_tuple)
				conf = getConfidence (itemSets, _tuple, right)
				if conf > c:
					associations[tuple([tuple(_tuple), tuple(right)])] = conf

		counter += 1

def generateAssociations (itemSets, c):
	associations = {}
	length = len (itemSets)
	for k in range(2, length):
		getAssociation (itemSets, k, c, associations)

	return associations

def printAssociations (associations):
	print ""
	print "Association rules generated from frequent itemsets: \n"
	for key in associations:
		left = key[0]
		right = key[1]
		conf = associations[key]
		print(str(left)+"\t->\t"+str(right)+"\tCONF: "+str(conf))
	
	print ""

def main ():
	c = 0.5
	results = AprioriAlgo ()
	print ""
	for i in range (1, len(results)):
		print "Frequent itemset of " + str(i) +"-tuples has length: " + str(len(results[i]))
		
		#for key in _dict.keys():
			#print "Key: " + str(key) + " - Value: " + str(_dict[key])

	associations = generateAssociations (results, c)
	printAssociations (associations)


if __name__ == "__main__":
	main ()
