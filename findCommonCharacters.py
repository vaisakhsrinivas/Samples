
from collections import Counter
def commonChars(words: List[str]) -> List[str]:

    firstwordcount = Counter(words[0]) # count the frequency of each character in the first word

    for word in words[1:]:
        wordfreq = Counter(word) # count the frequency of each character in the current word
        for c in firstwordcount:
            if c in wordfreq: # if the character is present in both words
                firstwordcount[c] = min(firstwordcount[c],wordfreq[c]) # update the count to the minimum of the two counts
            else:
                firstwordcount[c] = 0

    result = ''
    for c in firstwordcount:
        if firstwordcount[c] > 0:
            result += c * firstwordcount[c] # add the character to the result string the minimum number of times it occurs in the first word
    return list(result)


words = ["bella","label","roller"]
words2 = ["cool","lock","cook"]
print(commonChars(words))
print(commonChars(words2))