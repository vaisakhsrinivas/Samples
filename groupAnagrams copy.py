from collections import defaultdict

def groupAnagrams(words):

    group = defaultdict(list)

    for word in words:
        count = [0] * 26  # There are 26 letters in the English alphabet
        for char in word:
            count[ord(char) - ord('a')] += 1
        group[tuple(count)].append(word)
        print(group)  # Debug: print the current state of the group dictionary
    return group.values()  # returns the grouped anagrams

list_of_words = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(list_of_words))