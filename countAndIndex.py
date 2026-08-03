def countandindex(s):

    countindex = {}
    for i, char in enumerate(s):
        if char not in countindex:
            countindex[char] = {"count":0, "index": []}
        countindex[char]["count"] += 1
        countindex[char]["index"].append(i)
    return countindex

print(countandindex("Mississippi"))
