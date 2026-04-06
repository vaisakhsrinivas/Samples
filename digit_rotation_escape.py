def digit_rotation_escape(n):

    toString = str(n)
    length = len(toString)
    rotation = 0

    for _ in range(length):
        if int(toString)%length == 0:
            return rotation
        else:
            toString = toString[1:] + toString[0]
            rotation += 1
    return "none"

print(digit_rotation_escape(123))
print(digit_rotation_escape(13579))
print(digit_rotation_escape(24681))
print(digit_rotation_escape(84138789345))
