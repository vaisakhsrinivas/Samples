'''
Given a string representing a Roman numeral, return its integer value.

Roman numerals consist of the following symbols and values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Numerals are read left to right. If a smaller numeral appears before a larger one, the value is subtracted. Otherwise, values are added.

'''


def parse_roman_numeral(numeral):

    total = 0
    roman = {"I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000}

    for i in range(len(numeral)):
        if i+1 < len(numeral) and roman[numeral[i]] < roman[numeral[i+1]]:
            total -= roman[numeral[i]]
        else:
            total += roman[numeral[i]]
    return total


print(parse_roman_numeral("IV"))
print(parse_roman_numeral("III"))
print(parse_roman_numeral("XXVI"))
print(parse_roman_numeral("XCIX")) #should return 99.
print(parse_roman_numeral("CDLX")) #should return 460.
print(parse_roman_numeral("DIV")) #should return 504.
print(parse_roman_numeral("MMXXV")) #should return 2025.