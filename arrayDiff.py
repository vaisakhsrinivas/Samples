'''
Given two arrays with strings values, return a new array containing all the values that appear in only one of the arrays.

The returned array should be sorted in alphabetical order.
'''


def array_diff(arr1, arr2):

    set1 = set(arr1)
    set2 = set(arr2)
    result = []

    for a in arr1:
        if a not in set2:
            result.append(a)

    for a in arr2:
        if a not in set1:
            result.append(a)

    return sorted(result)


'''
result = []

    for a in arr1:
        if a not in arr2:
            result.append(a)
    
    for a in arr2:
        if a not in arr1:
            result.append(a)

    return sorted(result)
'''
