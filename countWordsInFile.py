import os


def countCheck(checkword, inputfile):
    """get word frquency from given file
       @param: checkword: word for which frequency needs to be returned
        
       @return: integer: word frequency
    """

    wordfrequency = {}

    if not os.path.isfile(inputfile):
        return 0

    if checkword == None or len(checkword) == 0 or not checkword.isalpha():
        return 0

    filesize = os.path.getsize(inputfile)
    if filesize == 0:
        return 0
    else :
        f = open(inputfile, 'r')
        for text in f:
            text = text.strip()
            words = text.split(" ")
            for w in words:
                if w.isalpha():
                    if w in wordfrequency:
                        wordfrequency[w] = wordfrequency[w] + 1
                    else:
                        wordfrequency[w] = 1

    if checkword in wordfrequency.keys():

        return wordfrequency[checkword]





