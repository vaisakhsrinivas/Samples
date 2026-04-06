def missingNumber(s):


    n = len(s)

    total = (n+1) * (n+2) // 2

    currentsum = sum(s)

    missing =  total -  currentsum

    return missing




print(missingNumber([1,2,4,5,6]))