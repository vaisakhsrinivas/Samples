def stringCompression(message):
    print(message)
    encoded_message = ""
    result = []
    i = 0

    if (len(message) == 1):
        return message
    else:
        while (i <= len(message)-1):
            count = 1
            ch = message[i]
            j = i
            while (j < len(message)-1):
                if (message[j] == message[j+1]):
                    count = count+1
                    j = j+1
                else:
                    break
            encoded_message=encoded_message+ch+str(count)
            i = j+1
        for i in encoded_message:
            result.append(i)
        return result



l = (stringCompression(["a","a","b","b","c","c","c"]))
print(l)
print(len(l))