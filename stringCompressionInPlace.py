def stringCompressionInPlace(chars):
        if not chars:
            return 0
        if len(chars) == 1:
            return 1

        i=0
        count = 1

        while i < len(chars) - 1:

            while i < len(chars) - 1 and chars[i]==chars[i+1]:
                count = count + 1
                chars.pop(i+1)
            if count > 1:
                for j in str(count):
                    chars.insert(i+1, j)
                    i+=1
                count=1
            i+=1
        print(chars)
        return(len(chars))




l = (stringCompressionInPlace(["a","a","b","b","c","c","c"]))
print(l)