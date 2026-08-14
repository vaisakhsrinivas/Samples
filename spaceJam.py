'''
Given a string, remove all spaces from the string,
insert two spaces between every character, convert all alphabetical letters to uppercase, and return the result.
Non-alphabetical characters should remain unchanged (except for spaces).
'''


def spaceJam(string):
    final = ""
    removespaces = string.replace(" ", "").upper()
    for i, char in enumerate(removespaces):
        if i > 0:
            final += "  "
        final += char
    return final


print(spaceJam("freeCodeCamp"))
print(spaceJam("   free   Code   Camp   "))
print(spaceJam("Hello World?!"))
print(spaceJam("C@t$ & D0g$"))
print(spaceJam("allyourbase"))