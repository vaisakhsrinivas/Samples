def count(l):

    d = dict()


    for i in l :
        if i in d:

            d[i] += 1

        else:

            d[i] = 1

    return d





l = [1,2,3,3,4,5,3,78,90,90]

print(count(l))

d = count(l)

print(sorted(d.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))