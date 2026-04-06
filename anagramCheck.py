
no_of_chars = 256

def checkAnagram(s1, s2):

    count = [0] * no_of_chars

    if len(s1) != len(s2):
        return False

    for i in s1:
        count[ord(i)] += 1

    for j in s1:
        count[ord(j)] -= 1


    for i in range(no_of_chars):
        if count[i] != 0:
            return False

    return True




s1 = "geeksforgeeks"
s2 = "forgeeksgeeks"

print(checkAnagram(s1, s2))