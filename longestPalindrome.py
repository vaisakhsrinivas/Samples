'''
You are given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.
'''


def longestPalindrome(s):

    seen = set()
    result = 0

    for char in s:
        if char in seen:
            seen.remove(char)
            result += 2
        else:
            seen.add(char)
    return result+1 if seen else result

print(longestPalindrome("ab")) #should return 1
print(longestPalindrome("a")) #should return 1
print(longestPalindrome("abccccdd")) #should return 7