# Write a function to find the largest odd integer in an array. For example, from [ 7, 9, 2, 10 ], return 9.?
# i/ps :

# input of mixed integers [-1,1,2,4] = 1
# input with float data type [1,3,4.5,2] = 3
# blank input = error msg  req added : saying i/p is blank
# all being same value = [3,3,3,3,3] = 3
# single value array also check if it is 0 = if 0 then not an odd integer. req : display no odd integer found.

# [ 7, 9, 2, 10 ] - 9
#

def maxodd(n):

    odd = []

    len_n = len(n)

    max_odd = -1

    if len_n == 1:
        if ((n[0]%2) != 0) :
            #odd.append[n[i]]
            print(n[0])
        else:
            print("No an odd number")
    elif len_n > 1:

        for i in range(len_n):
            if ((n[i] % 2) != 0) and isinstance(n[i], int) and n[i] > max_odd:
                max_odd = n[i]
        print(max_odd)
                #odd.append(n[i])

    len_odd = len(odd)
    if len_odd > 0:
        odd.sort(reverse=True)
        print(odd[0])


a = [1,3,4,4.5]
maxodd(a)
