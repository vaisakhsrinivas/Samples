'''
Given an integer, determine if that number is a prime number or a negative prime number.

A prime number is a positive integer greater than 1 that is only divisible by 1 and itself.
A negative prime number is the negative version of a positive prime number.
1 and 0 are not considered prime numbers.
'''

import math
def unnaturalPrime(number):

    if number in [-1, 0, 1]:
        return False

    number = abs(number)

    if number == 2:
        return True
    if number % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True
print((unnaturalPrime(1))) #should return False.
print((unnaturalPrime(-1))) #should return False.
print((unnaturalPrime(19))) #should return True.
print((unnaturalPrime(-23))) #should return True.
print((unnaturalPrime(0))) #should return False.
print((unnaturalPrime(97))) #should return True.
print((unnaturalPrime(-61))) #should return True.
print((unnaturalPrime(99))) #should return False.
print((unnaturalPrime(-44))) #should return False.
