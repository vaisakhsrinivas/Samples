def checkValidity (s):

    s = s.split(".")

    for i in s:

        if  (len(i) > 3  and int(i) < 0 or int(i) > 255):

            return False

        if (len(i) > 1 and int(i) == 0):
            return False

        if (len(i) > 1 and int(i) !=0  and i[0] == '0'):

            return False


    return True



def convert(ip):

    lenip = len(ip)

    if lenip > 12:

        return []

    newip = ip
    l = []


    for i in range(1, lenip-2):

        for j in range(i+1, lenip-1):

            for k in range(j+1, lenip):

                newip = newip[:k] + "." + newip[k:]
                newip = newip[:j] + "." + newip[j:]
                newip = newip[:i] + "." + newip[i:]


                if checkValidity(newip):
                    l.append(newip)

                newip = ip

    return l



A = "25525511135"
#B = "25505011535"

print(convert(A))
#print(convert(B))