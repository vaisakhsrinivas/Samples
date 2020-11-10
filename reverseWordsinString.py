
def reverse_words(s, start, end):

    while start < end:

        s[start], s[end] = s[end], s[start]

        start = start + 1
        end = end - 1


s = str(input())

s = list(s)

start = 0


while True:

    try:

        end = s.index(" ", start)

        reverse_words (s, start, end-1)

        start = end + 1

    except ValueError:

        reverse_words(s, start, len(s)-1)

        break

print(s)

s = "".join(s)

print(s)

#s.reverse()

s = "".join(s)

print (s)

