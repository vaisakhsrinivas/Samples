def longestPalindromicSubstring(s):

    slen = len(s)

    low = 0
    high = 0

    maxlen = 1

    start = 0


    for i in range(1, slen):

        low = i-1
        high = i

        while low >= 0 and high < slen and s[low] ==  s[high]:

            if high-low+1 > maxlen:
                start = low
                maxlen =  high-low+1

            low = low - 1
            high = high + 1

        low = i-1
        high = i+1

        while low >= 0 and high < slen and s[low] ==  s[high]:

            if high-low+1 > maxlen:
                start = low
                maxlen =  high-low+1

            low = low - 1
            high = high + 1

    print("Longest Palindromic Substring is")
    print(s[start:start + maxlen])

    return maxlen




print(longestPalindromicSubstring("forgeeksskeegfor"))