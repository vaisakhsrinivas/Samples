'''
Given an array and a chunk size, return the array split into sub-arrays of that size.

The last chunk may be smaller if the array doesn't divide evenly.
'''

def chunkSize(array, chunkSize):

    result = []
    for i in range (0, len(array), chunkSize):
        result.append(array[i:i+chunkSize])
    return result

print(chunkSize([1, 2, 3, 4, 5, 6], 3)) #should return [[1, 2, 3], [4, 5, 6]].
print(chunkSize([1, "two", 3, "four", 5, "six", 7, "eight"], 2)) #should return [[1, "two"], [3, "four"], [5, "six"], [7, "eight"]].
print(chunkSize([1, 2, 3, 4, 5], 3)) #should return [[1, 2, 3], [4, 5]].
print(chunkSize(["a", "b", "c", "d", "e"], 1)) #should return [["a"], ["b"], ["c"], ["d"], ["e"]].
print(chunkSize([1, 2, 3], 5)) #should return [[1, 2, 3]].