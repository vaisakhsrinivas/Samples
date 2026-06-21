'''
Given an integer greater than 1, return its prime factorization as an array of numbers in ascending order.

A prime factorization is the set of prime numbers that multiply together to produce the given integer. Each number has exactly one set. For example, the prime factorization of 20 is [2, 2, 5] because 2 * 2 * 5 = 20.

If the given integer is itself prime, return it in a single-element array.
'''

def primeFactors(n):
    factors = []
    primeDivisor = 2

    while primeDivisor * primeDivisor < n:
        while n % primeDivisor == 0:
            factors.append(primeDivisor)
            n //= primeDivisor
        primeDivisor += 1

    if n > 1:
        factors.append(n)
    return factors

primefactors = primeFactors(10)
print(primefactors)
#output - [2, 5]
primefactors = primeFactors(20)
print(primefactors)
#output - [2, 2, 5]
primefactors = primeFactors(17)
print(primefactors)
#output - [17]
primefactors = primeFactors(15)
print(primefactors)
#output - [3, 5]
primefactors = primeFactors(35)
print(primefactors)
#output - [5, 7]
primefactors = primeFactors(99)
print(primefactors)
#output - [3, 3, 11]
primefactors = primeFactors(360)
print(primefactors)
#output - [2, 2, 2, 3, 3, 5]
primefactors = primeFactors(510510)
print(primefactors)
#output - [2, 3, 5, 7, 11, 13, 17]