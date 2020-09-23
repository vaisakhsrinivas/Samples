def add(s1, s2):

    res = []

    p1 = len(s1) - 1
    p2 = len(s2) - 1

    carry = 0

    while p1 >= 0 or p2 >=0:

        x1 = ord(s1[p1]) - ord('0') if p1 >= 0 else 0
        x2 = ord(s2[p2]) - ord('0') if p2 >= 0 else 0

        value = (x1 + x2 + carry) % 10
        carry = (x1 + x2 + carry) // 10
        res.append(value)
        p1 = p1 - 1
        p2 = p2 - 1


    if carry:
        res.append(carry)

    return ''.join(str(x) for x in res[::-1])



num1 = "900"
num2 = "100"

print(add(num1,num2))