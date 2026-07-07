'''
Given two integers, round the first to the nearest multiple of the second.
'''

def nearestMultiple(num, multiple):

    return round(num / multiple) * multiple



print(nearestMultiple(5, 3)) #should return 6.
print(nearestMultiple(17, 4)) # should return 16.
print(nearestMultiple(43, 5)) # should return 45.
print(nearestMultiple(38, 11)) # should return 33.
print(nearestMultiple(93, 12)) # should return 96.