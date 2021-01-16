def seperate(arr, l):
    j = 0
    for i in range(l):

        if arr[i] <= 0:

            arr[i], arr[j] = a[j], arr[i]
            j = j + 1
    return j


def positivenumber(arr, l):

    for i in range(l):

        if (abs(arr[i])-1 <l and arr[abs(arr[i])-1] > 0):
            arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]

    for i in range(l):

        if arr[i] > 0:

            return i+1
    return l+1


def missingnumber(arr, l):

   s = seperate(arr , l)

   return positivenumber(arr[s:], l-s)





a = [0,-10,-2,-1,-20]
l = len(a)
print(missingnumber(a, l))