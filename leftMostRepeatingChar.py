def leftMostRepeating(s):
    l = len(s)
    visited = set()
    for i in range(l):
        if s[i] not in visited:
            visited.add(s[i])
            if s.count(s[i]) != 1 and s[i] in visited:
                return i
    return -1


print(leftMostRepeating("abcdeffjkll"))