def calculateTime(keyboard: str, word: str) -> int:
    d = {}
    for i in range (len(keyboard)):
        d[keyboard[i]] = i

    result = 0
    tmp = 0

    for i in word:
        result += abs(d[i] - tmp)
        tmp = d[i]
    return result




keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"

print(calculateTime(keyboard, word))