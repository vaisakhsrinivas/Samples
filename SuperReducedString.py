import sys

def super_reduced_string(s):

    count =0;
    for i in range(0, len(s)-1, 1):
        j = i+1
        if s[i]==s[j]:
            count = count + 1

            if count%2 == 0:
                s.replace(s[i],"")
                s.replace(s[j],"")

        elif len(s) == 0:
            print("Empty String")
    return s



s = input().strip()
result = super_reduced_string(s)
print (result)