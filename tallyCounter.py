'''
Given a string of tally marks, return the total count represented.

Each pipe "|" represents one count.
Every fifth mark is represented as a forward slash "/", completing a group of five ("||||/").
Groups are separated by a space.
'''


def get_tally_count(s):
    count = 0
    for c in s:
        if c != " ":
            count += 1
    return count


print(get_tally_count("||||/"))   # 5
print(get_tally_count("||||/ ||||/")) # 10
print(get_tally_count("||||/ |||")) # 8
print(get_tally_count("||||/ ||||/ ||||/ ||")) # 17
print(get_tally_count("||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ ||||/ |")) # 41