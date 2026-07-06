'''
Given a string, return only the words that are entirely lowercase,
in their original order and with a space between each word.
'''


def lowercase(s):

    result = []
    s = s.split()
    for word in s:
        if word.islower():
            result.append(word)
    return " ".join(result)


print(lowercase("hello GOOD world")) # should return "hello world".
print(lowercase("these are all lowercase")) # should return "these are all lowercase".
print(lowercase("less is NoT more")) # should return "less is more".
print(lowercase("DonT eat pizza every OTHER day")) #should return "eat pizza every day".
print(lowercase("the Super quick AND snEaky brown fox Leapt anD jumped over aNd AROUND the lazy SloW dog")) #should return "the quick brown fox jumped over the lazy dog".