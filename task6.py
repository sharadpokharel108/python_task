#Two sum problem

def two_sum(array, target):
	seen={}
	for i,x in enumerate(array):
		competent=target-x
		if competent in seen:
			return [seen[competent], i]
		seen[x]=i

	return []


print(two_sum([2,7,11,15], 18))