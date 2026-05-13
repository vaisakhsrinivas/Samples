def offendingElement(element):

    for i in range(1, len(element)):
        if element[i-1] > element[i]:
            if i > 1 and element[i-2] > element[i]:
                return i
            return i-1
    return None



print(offendingElement([1, 6, 2, 3, 4, 5]))
print(offendingElement([1, 2, 3, 5, 4, 5]))
print(offendingElement([2, 1]))
print(offendingElement([2, 4, 1, 6, 8]))
print(offendingElement([5, 18, 24, 33, 40, 55, 15, 68, 84, 91]))