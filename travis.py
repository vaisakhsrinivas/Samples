knownusers = ["Alice", "Bob", "Emma", "Dan", "Fred", "Harry", "Georgie", "Claire" ]


while True:
    print("Hi, My name is Travis")
    name = input("Whats your name ?:").strip().capitalize()

    if name in knownusers:
        print("Hello {}".format(name))
        remove = input("Would you like to be removed or not (y/n)?:").strip().lower()

        if remove == "y":
            knownusers.remove(name)
        elif remove == "n":
            print("Thanks for staying")
    else:
        print("Sorry {}. Your name is not in the list".format(name))
        add = input("Would you like to be added ? (y/n):").strip().lower()
        if add == "y":
            knownusers.append(name)
        elif add == "n":
            print("Well, see you around")


