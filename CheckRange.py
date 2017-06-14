def checkrange(number):
    if number in range(0,100):
        print("number in range")
    else:
        print("number out of range")

number = int(input("Enter the number"))
checkrange(number)