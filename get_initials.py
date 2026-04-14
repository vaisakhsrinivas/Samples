def get_initials(name):
    splt = name.split()
    initials = ""
    for i in splt:
        initials += i[0].upper()
    return ".".join(initials)+"."

def pythonic_get_initials(name):
    return ".".join(name[0].upper() for name in name.split()) + "."

if __name__ == "__main__":
    print(get_initials("Tommy Millwood"))
    print(pythonic_get_initials("Tommy Millwood"))
