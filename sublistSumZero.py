def subslist(l):


    d = dict()
    totalsum = 0

    for i in l:
        totalsum = totalsum + i

        if totalsum is 0 or i is 0 or d.get(totalsum) is not None:

            return True

        d[totalsum] = i

    return False


my_list = [6, 4, -7, 3, 12, 9]

print(subslist(my_list))
