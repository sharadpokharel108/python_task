# Flatten a nested list of arbitrary depth.

def flatten(my_list):
	final_list=[]
	for x in my_list:
		if type(x)==list:
			final_list.extend(flatten(x))
		else:
			final_list.append(x)
	return final_list

print(flatten([1, 2, [3, 4], 5, [6, 7, 8], 9]))