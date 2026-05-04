# Print the first non-repeated character in a string, return None if there is no such character.

input= "aaaabbaccded"

# for x in input:
#     if input.count(x) == 1:                  #Trick: We can use the count method to check if a character is repeated or not. If the count is 1, it means it's not repeated. 
#         print(x)
#         break


#next trick

from collections import Counter

count=Counter(input)

gen=(ch for ch in input if count[ch]==1)            #Trick: We can use a generator expression to iterate through the string and check if the count of each character is 1. If it is, we yield that character. Then we can use the next function to get the first non-repeated character. If there is no such character, we can return None by passing None as the second argument to next.

print(next(gen,None))