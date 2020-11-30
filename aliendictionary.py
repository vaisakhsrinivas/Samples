def aliendictionary (words, order):

    d = dict()

    for i, c in enumerate(order):
        d[c] = i

    for i in range(len(words)-1):
        w1 = words[i]
        w2 = words[i+1]

        if w1 == w2:
            continue

        if len(w1) > len(w2):
            if w1.startswith(w2):
                return False

        for j in range(min(len(w1), len(w2))):
            if d.get(w1[j]) < d.get(w2[j]):
                break
            elif d.get(w1[j]) == d.get(w2[j]):
                continue
            else:
                return False

    return True


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

print (aliendictionary(words, order))