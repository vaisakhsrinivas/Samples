def palindrom(s):

    r = ""

    for i in s:

        r = i + r


    if s == r:

        print ("Palindrome")

    else:

        print ("Not palindrome")



palindrom("malayala")