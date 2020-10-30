def topkelements(s, k):


    wordcount = dict()


    for word in s:


        if word not in wordcount:

            wordcount[word] = 1

        else:

            wordcount[word] += 1


    result = [[k,v] for k,v in wordcount.items()]

    result.sort()

    result.sort(key= lambda x:x[1], reverse=True)


    return [item[0] for item in result][:k]



s = ["i", "love", "leetcode", "i", "love", "coding"]

k = 2

print(topkelements(s,k))
