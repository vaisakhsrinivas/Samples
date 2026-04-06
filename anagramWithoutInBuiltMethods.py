
no_of_chars = 256

def checkAnagram(s1, s2):

    count1 = [0] * no_of_chars
    count2 = [0] * no_of_chars

    for i in s1:
        count1[ord(i)] += 1

    for j in s2:
        count2[ord(j)] += 1

    if len(s1) != len(s2):
        return False

    for i in range(no_of_chars):
        if count1[i] != count2[i]:
            return False

    return True




s1 = "geeksforgeeks"
s2 = "forgeeksgeeksfw"

print(checkAnagram(s1, s2))