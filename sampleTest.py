def findDuplicateCharacters(s):


    l = len(s)


    d = dict()



    for i in range (l):

        if s[i] not in d:

            d[s[i]] = 1

        else:

            d[s[i]] = d[s[i]] + 1





    for i,k in d.items():

        if k > 1:

            print (i,k)




word = "heellooo"

findDuplicateCharacters(word)




