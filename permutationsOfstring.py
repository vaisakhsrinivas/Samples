
def permutations (a, l, r):

    if (l==r):

        print("".join(a))

    else:

        for i in range(l, r+1):

            a[l], a[i] = a[i], a[l]
            permutations(a, l+1, r)
            a[l], a[i] = a[i], a[l]


s = "ABC"

l = len(s)
a = list(s)

permutations(a, 0, l-1)