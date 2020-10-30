def longest_substring_with_k_distinct(s, k):


    start = 0

    maxlen = 0

    d = dict()


    for end in range(len(s)):

        right =  s[end]

        if right not in d:

            d[right] = 1

        else:

            d[right] += 1

        while len(d) > k:

            left = s[start]

            d[left] = d[left] - 1

            if d[left] == 0:
                del d[left]

            start = start + 1

        maxlen = max (maxlen, end-start+1)

    return maxlen





print(longest_substring_with_k_distinct("araaci", 2))