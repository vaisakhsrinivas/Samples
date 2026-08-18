'''
Given an integer n, return true if and only if it is an Armstrong number.

The k-digit number n is an Armstrong number if and only if the kᵗʰ power of each digit sums to n.
'''


def amstrongNumber(n):

    cube = 0
    digits = [int(i) for i in str(n)]
    l = len(digits)
    for i in digits:
        cube += i**l
    if cube == n:
        return True
    else:
        return False

print(amstrongNumber(153))
print(amstrongNumber(123))