def groupAnagrams(words):

    group = {}

    for word in words:
        sortedword = ''.join(sorted(word))
        group[sortedword] = group.get(sortedword,[]) + [word]

    #return group #returns the dictionary
    return group.values() #returns the grouped anagrams



list_of_words = ["act","pots","tops","cat","stop","hat"]
print(groupAnagrams(list_of_words))