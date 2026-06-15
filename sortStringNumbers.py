'''
Given a string of numbers separated by commas, return an array of the numbers sorted from smallest to largest.
'''


def sort_numbers(s):

    result = []
    for n in s.split(','):
        result.append(int(n))
    result.sort()
    return result

    # return sorted(int(x.strip()) for x in s.split(","))


print(sort_numbers("3,1,2")) #should return [1, 2, 3].
print(sort_numbers("5,3,8,1,9,2")) # should return [1, 2, 3, 5, 8, 9].
print(sort_numbers("12,61,49,80,19,50,77,38")) #should return [12, 19, 38, 49, 50, 61, 77, 80].
print(sort_numbers("0,6,-19,44,-2,7,0")) # should return [-19, -2, 0, 0, 6, 7, 44].
