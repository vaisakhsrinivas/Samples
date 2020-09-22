def lps (s, i, j):


    if i == j:
        return 1

    if s[i] == s[j] and j == i+1:
        return 2

    if s[i] == s[j]:
        return lps(s, i+1, j-1) + 2

    return max(lps(s, i, j-1 ),lps(s,i+1,j))


s = "geeksforgeeks"
n = len(s)
print(lps(s, 0, n-1))
