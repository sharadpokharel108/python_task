# Find the missing number in a list of integers from 1 to n. The list has n-1 numbers, and there are no duplicates.

#Trick:1--> sum of n natural numbers is n(n+1)/2

import array


def missing_1(array, n):
	sum_of_n= n*(n+1)/2
	sum_of_array=sum(array)                     #trick is just difference the sum to get the missing number
	return sum_of_n-sum_of_array



#Trick:2--> Xoring same number twice will make the result 0, if we xor all the numbers from 1 to n and then xor with all the numbers in the array, we will get the missing number
def missing_2(array, n):
    xor_array = 0
    xor_num = 0

    for i in range(1, n+1):
        xor_num ^= i

    for i in array:
        xor_array ^= i

    return xor_num ^ xor_array


#Trick:3-->Set differnce method

def missing_3(array, n):
    set_full = set(range(1, n+1))
    set_array = set(array)
    missing_number = set_full - set_array
    return missing_number.pop() if missing_number else None


print(missing_1([1,2,3,5], 5))
print(missing_2([1,2,3,5], 5))
print(missing_3([1,2,3,5], 5))