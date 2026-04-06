def leftRotate(a,n):

    numberOfRotations = int(n)
    lengthOfArray = len(a)
    tmp = [0]*numberOfRotations

    for i in range (numberOfRotations):
        tmp[i] = a[i]
    for i in range (numberOfRotations,lengthOfArray):
        a[i-numberOfRotations] = a[i]
    for i in range (numberOfRotations):
        a[lengthOfArray-numberOfRotations+i] = tmp[i]

    return a





a = [5,6,7,8,10]
n = input("Enter number of rotations")
print(leftRotate(a,n))