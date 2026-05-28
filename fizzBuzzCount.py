'''
Given a start and end number, count the number of fizz and buzz appearances in the range (inclusive).

Numbers divisible by 3 count as a fizz.
Numbers divisible by 5 count as a buzz.
Numbers divisible by both 3 and 5 count as both a fizz and a buzz.
Return an object or dictionary with the counts in the format: { fizz, buzz }.
'''


def fizz_buzz_count(start, end):
    countfizz = 0
    countbuzz = 0
    countdict = {"fizz": countfizz, "buzz": countbuzz}

    for i in range(start, end + 1):
        if i % 3 == 0:
            countfizz += 1
        if i % 5 == 0:
            countbuzz += 1
    countdict["fizz"] = countfizz
    countdict["buzz"] = countbuzz
    return countdict

print(fizz_buzz_count(1, 11)) # should return {"fizz": 3, "buzz": 2}.
print(fizz_buzz_count(14, 41)) #should return {"fizz": 9, "buzz": 6}.
print(fizz_buzz_count(24, 100)) #should return {"fizz": 26, "buzz": 16}.
print(fizz_buzz_count(-635, -14)) #should return {"fizz": 207, "buzz": 125}.
print(fizz_buzz_count(-5432, 6789)) #should return {"fizz": 4074, "buzz": 2444}.