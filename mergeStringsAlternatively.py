class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lw1 = len(word1)
        lw2 = len(word2)
        i = 0
        j = 0
        mergeString = ""
        word = 1

        while i < lw1 and j < lw2:
            if word == 1:
                #mergeString.append(word1[i])
                mergeString = mergeString + word1[i]
                i += 1
                word = 2
            else:
                #mergeString.append(word2[j])
                mergeString = mergeString + word2[j]
                j += 1
                word = 1

        while i < lw1:
            #mergeString.append(word1[i])
            mergeString = mergeString + word1[i]
            i += 1

        while j < lw2:
            #mergeString.append(word2[j])
            mergeString = mergeString + word2[j]
            j += 1

        #return ''.join(mergeString)
        return mergeString


c = Solution()
word1 = "abc"
word2 = "pqr"
print(c.mergeAlternately(word1, word2))