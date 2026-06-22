'''
Given a lowercase string, return it translated into leet speak by replacing the letters below with their leet substitutions:

Letter	Leet
a	4
e	3
g	9
i	1
l	1
o	0
s	5
t	7
Characters with no substitution are left unchanged.
'''

def leetSpeak(string):
    letter = {"a": "4", "e": "3", "g": "9", "i": "1", "l": "1", "o": "0", "s": "5", "t": "7"}
    result = []
    for char in string:
        if char in letter:
            result.append(letter[char])
        else:
            result.append(char)
    return "".join(result)


print(leetSpeak("cool")) #return "c001".
print(leetSpeak("leet"))  #return "1337".
print(leetSpeak("hacker"))  #return "h4ck3r".
print(leetSpeak("satellite"))  #return "547311173".
print(leetSpeak("abcdefghijklmnopqrstuvwxyz")) #return "4bcd3f9h1jk1mn0pqr57uvwxyz"