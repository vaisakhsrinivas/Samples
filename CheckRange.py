def checkrange(number, low, high):
    if number in range(low,high):
        print("number in range")
    else:
        print("number out of range")

number = int(input("Enter the number"))
checkrange(number)