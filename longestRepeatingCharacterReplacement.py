def characterReplacement(s, k):


    l = len(s)
    start = 0
    max_count = 0
    max_len = 0

    d = {}

    for end in range(l):

        if s[end] not in d:
            d[s[end]] = 1
        else:
            d[s[end]] += 1

        max_count = max(max_count, d[s[end]])

        if (end - start - max_count + 1 > k):

            d[s[start]] -= 1
            start = start + 1

        max_len = max(max_len, end-start+1)

    return max_len



s = "ABAB"
k = 2

print(characterReplacement(s,k))