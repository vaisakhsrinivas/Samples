def firstUnique(s):
    l = len(s)
    visited = set()
    for i in range(l):
        if s[i] not in visited:
            visited.add(s[i])
            if s.count(s[i]) == 1:
                return i
    return -1


print(firstUnique("eetcode"))