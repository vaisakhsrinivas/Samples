def reverse(s):
    r = ""

    for i in s:

        r = i + r

    return r


print(reverse("geeks quiz practice code"))