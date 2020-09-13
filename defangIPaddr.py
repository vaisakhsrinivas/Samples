def defangIPaddr(address):
    address = address.replace(".","[.]")
    return address



addr = "1.1.1.1"
print(defangIPaddr(addr))