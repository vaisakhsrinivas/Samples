
def reverseString(s):
    reverse = []

    for i in range (len(s)):
        if s[i] != " ":
            reverse.append(s[i])

        else:

            while len(reverse) > 0:
                print(reverse[-1], end="")
                reverse.pop()
            print(end= " ")

    while len(reverse) > 0:
        print(reverse[-1], end="")
        reverse.pop()



s = "Geeks for Geeks"

reverseString(s)
