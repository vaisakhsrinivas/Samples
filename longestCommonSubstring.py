'''
Given a string, return the longest substring that appears more than once.

The substrings can overlap.
'''

def get_longest_substring(s):

    s = s.strip()
    n = len(s)

    for length in range(n-1, 0, -1):
        seen = set()
        for i in range(n-length+1):
            sub = s[i:i+length]
            if sub in seen:
                return sub
            seen.add(sub)
    return ''


print(get_longest_substring("abracadabra"))
print(get_longest_substring("hello world hello"))
print(get_longest_substring("mississippi"))
print(get_longest_substring("ha ha ha ha ha ha ha"))
print(get_longest_substring("the quick brown fox jumped over the lazy dog that the quick brown fox jumped over"))