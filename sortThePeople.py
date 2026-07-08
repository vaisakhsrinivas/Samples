'''
You are given an array of strings names, and an array heights that consists of distinct positive integers.
Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the i-th person.

Return names sorted in descending order by the people's heights.
'''


def sortPeople(names, heights):

    heightToName = {}
    result = []

    for h,n in zip(heights,names):
        heightToName[h] = n

    for height in reversed(sorted(heights)):
        result.append(heightToName[height])

    return result

names = ["Mary","John","Emma"]
heights = [180,165,170]
print(sortPeople(names,heights))
names = ["Alice","Bob","Bob"]
heights = [155,185,150]
print(sortPeople(names,heights))