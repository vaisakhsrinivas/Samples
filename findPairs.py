def findpairs(n):


    d = dict()

    result = []

    for i in range(len(n)):

        for j in range(i+1, len(n)):

            added = n[i]  +  n[j]

            if added not in d:

                d[added] =  [n[i], n[j]]

            else:

                previouspair = d.get(added)

                secondpair = [n[i], n[j]]

                result.append(previouspair)
                result.append(secondpair)

                return result


    return result


my_list = [3, 4, 7, 1, 12, 9, 0]
print(findpairs(my_list))