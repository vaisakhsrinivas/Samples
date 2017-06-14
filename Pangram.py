import string

def ispangram(string, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(string.lower())


string = str(input("Enter the string"))
print(ispangram(string))