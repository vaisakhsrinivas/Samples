'''
You are given a string s consisting only of the characters '0' and '1'.
In one operation, you can change any '0' to '1' or vice versa.

The string is called alternating if no two adjacent characters are equal.
For example, the string "010" is alternating, while the string "0100" is not.

Return the minimum number of operations needed to make s alternating.
'''

def minimumOperations(s):

    count=0
    for i in range(len(s)):
        if i%2==0:
            count+=1 if s[i]=='0' else 0
        else:
            count+=1 if s[i]=='1' else 0
    return min(count,len(s)-count)


print(minimumOperations("0100"))
print(minimumOperations("10"))
print(minimumOperations("1111"))