'''
Given two DNA strands of equal length, return an array of indexes where the strands differ (mutations).

DNA strands are strings made up of the characters "A", "T", "C", and "G"
Return the indexes in ascending order
If there are no mutations, return an empty array
'''


def detectMutations(s1, s2):

    result = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            result.append(i)
    return result


print(detectMutations("ATCG", "ATGG"))
print(detectMutations("ATGCGTACGTTAGC", "ATGCATACGATTGC"))
print(detectMutations("GATCTAGCTAGGCTAGCTAG", "GATCTAGCTAGGCTAGCTAG"))
print(detectMutations("TCAGATCATGGCTAGCTACGATCAGCTAGCATGCATATCGACTG", "TCAGATCATGGCTAGAGCTGATCAGCTAGCATGCATATCGACTG"))
print(detectMutations("ACGTCAGTACGCACATGACCATTGACATA", "AACGTCAGTACGCACATGACCATTGACAT"))