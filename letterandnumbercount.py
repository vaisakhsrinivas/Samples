def letterAndNumberCount(s):

    letterCount = 0
    numberCount = 0

    for char in s:
        if char.isalpha():
            letterCount += 1
        if char.isdigit():
            numberCount += 1
        lword = "letter" if letterCount == 1 else "letters"
        nword = "number" if numberCount == 1 else "numbers"
    return f"The string has {letterCount} {lword} and {numberCount} {nword}."


print(letterAndNumberCount("helloworld123")) #should return "The string has 10 letters and 3 numbers."
print(letterAndNumberCount("Catch 22")) #should return "The string has 5 letters and 2 numbers."
print(letterAndNumberCount("A1!")) #should return "The string has 1 letter and 1 number."