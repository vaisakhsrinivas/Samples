def makeAnagram(a,b):

    d = dict()

    for i in a:

        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    for i in b:

        if i in d:
            d[i] -= 1
        else:
            d[i] = -1


    diff = 0

    for j in d.keys():

        diff = diff + abs(d[j])

    return diff




a = "cde"
b = "abc"

print(makeAnagram(a,b))
