def digitRotationEscape(n):

    s = str(n)
    l = len(s)
    rotation = 0

    for _ in range(l):
        if int(s)%l == 0:
            return rotation
        else:
            s = s[1:] + s[0]
            rotation += 1
    return "none"

print(digitRotationEscape(123))
print(digitRotationEscape(13579))
print(digitRotationEscape(123456789))
print(digitRotationEscape(24681))
print(digitRotationEscape(84138789345))