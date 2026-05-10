'''
Given a string, determine if it is a valid ISBN-13 number.

A valid ISBN-13:

Contains only digits and hyphens
Has exactly 13 digits after removing hyphens
Passes the following check:
Multiply each digit by 1 or 3, alternating (multiply the first digit by 1, the second by 3, the third by 1, and so on).
The sum of the results must be divisible by 10.

'''

def isbnValidator(isbn):

    if not all (c.isdigit() or c == "-" for c in isbn):
        return False
    numbers = isbn.replace("-", "")
    if len(numbers) != 13:
        return False
    total = sum(int(d) * (1 if i%2 == 0 else 3) for i, d in enumerate(numbers))
    return total % 10 == 0

print(isbnValidator("9780306406157"))
print(isbnValidator("978-030-64061A-4"))





