'''
Given an integer between 1 and 10,000,
return a count of how many numbers from 1 up to that integer whose square contains at least one digit 3.
'''


def squares_with_three(n):
    return sum(1 for i in range(1, n+1) if "3" in str(i*i))


print(squares_with_three(10000))
print(squares_with_three(100))
print(squares_with_three(1000))
print(squares_with_three(0))
print(squares_with_three(10))