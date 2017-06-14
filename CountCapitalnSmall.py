def count(s):
    small = 0
    caps = 0
    for c in s:
        if c.isupper():
            caps+=1
        elif c.islower():
            small+=1
        else:
            pass
    print("number of caps", caps)
    print("number of small", small)

s = input("Enter the string")
count(s)
