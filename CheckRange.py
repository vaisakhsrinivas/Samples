def checkrange(number, low, high):
    if number in range(low,high):
        print("number in range")
    else:
        print("number out of range")

number = int(input("Enter the number"))
low = int(input("Enter the number"))
high = int(input("Enter the number"))
checkrange(number, low, high)