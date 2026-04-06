def sortArrayByParity(A):
    i,j=0,len(A)-1
    while i<j:
        if A[i]%2!=0:
            A[i],A[j]=A[j],A[i]
            j-=1
        else:
            i+=1
    return A


a = [3,1,2,4]
print(sortArrayByParity(a))