# Merge intervals

def my_func(n):
	return n[0]

my_list= [[8,10], [1,3], [2,6]]
new_list=sorted(my_list, key=my_func)            # ensure the list is sorted based on the start of the intervals

merged=[]

for interval in new_list:

	if not merged or merged[-1][1]<interval[0]:
		merged.append(interval)
	

	else:
		merged[-1][1]=max(merged[-1][1],interval[1])

print(merged)
