
def permutations (a, l, r):

    #d = dict()
    if (l==r):

        print("mycommand", " ".join(a))
       # d["mycommand", " ".join(a)] = 1
        #print(d.keys())

    else:

        for i in range(l, r+1):

            a[l], a[i] = a[i], a[l]
            permutations(a, l+1, r)
            a[l], a[i] = a[i], a[l]


#s = "ABC"

s = ["-a", "-b", "-c", "-d"]
l = len(s)
#a = list(s)

permutations(s, 0, l-1)