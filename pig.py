sentence = input("enter the sentence").lower().strip()

words = sentence.split()

newwords = []

for w in words:
    if w[0] in "aeiou":
        newword = w + "yay"
        newwords.append(newword)
    else:
        vowel_pos = 0
        for letter in w:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break

        cons = w[:vowel_pos]
        the_rest = w[vowel_pos:]
        newword = the_rest+cons+"ay"
        newwords.append(newword)

output = " ".join(newwords)
print(output)
