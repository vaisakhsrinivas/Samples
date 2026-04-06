MAX = 256

def compare (arr1, arr2):
    for i in range(MAX):
        if arr1[i] != arr2[i]:
            return False
        return True


def search (p,t):

    m = len(p)
    n = len(t)

    count_p = [0]*MAX
    count_t = [0]*MAX


    for i in range(m):
        count_p[ord(p[i] )] += 1
        count_t[ord(t[i])] += 1

    for i in range(m, n):

        if compare(count_p, count_t):
            print("Found at index", (i-m))

        count_t[ord(t[i])] += 1
        count_t[ord(t[i-m])] -= 1

    if compare(count_p, count_t):
        print("Found at index", n-m)



txt = "BACDGABCDA"
pat = "ABCD"
search(pat, txt)


