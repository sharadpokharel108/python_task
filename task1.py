# Write a function that groups words that are anagrams.
# Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output:
# [
#  ["eat", "tea", "ate"],
#  ["tan", "nat"],
#  ["bat"]
# ]



#Trick: We will use the trick that for every word we will make a key that will be same for all anagrams, and then append the words
# The key can be made in two ways: sorting the anagram, counting the frequency of characters in the anagram

from collections import defaultdict

def create_key_idea1(word):
    return ''.join(sorted(word))

def create_key_idea2(word):
    count = [0] * 26
    for char in word:
        count[ord(char) - ord('a')] += 1
    return tuple(count)


def group_anagrams(words):
    anagram_dict = defaultdict(list)
    for word in words:
        key = create_key_idea1(word)  # You can switch to create_key_idea2 if you prefer
        anagram_dict[key].append(word)
    return list(anagram_dict.values())