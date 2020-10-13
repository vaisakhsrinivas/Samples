def symmetricPair(s):

    pairset = set()

    result = []

    for pair in s:

        pairtup = tuple(pair)
        pair.reverse()
        reversetup =  tuple(pair)


        if reversetup in pairset:

            result.append(list(pairtup))
            result.append(list(reversetup))

        else:

            pairset.add(pairtup)

    return result



arr = [[1, 2], [4, 6], [4, 3], [6, 4], [5, 9], [3, 4], [9, 5]]
symmetric = symmetricPair(arr)
print(symmetric)