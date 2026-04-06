def urlifyString(s):

    s = s.strip()
    l = len(s)
    newstr = ""

    for i in range (0, l):

        if s[i] == " ":

            newstr = newstr + '%20'

        else:

            newstr = newstr + s[i]

    return newstr




print(urlifyString("    Cracking the coding interview    "))

