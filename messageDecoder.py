'''
Given a secret message string, and an integer representing the number of letters that were used to shift the message to encode it, return the decoded string.

A positive number means the message was shifted forward in the alphabet.
A negative number means the message was shifted backward in the alphabet.
Case matters, decoded characters should retain the case of their encoded counterparts.
Non-alphabetical characters should not get decoded.
'''

def messageDecoder(message: str, shift: int) -> str:

    result = []
    for char in message:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decoded = (ord(char)-base-shift)%26+base
            result.append(chr(decoded))
        else:
            result.append(char)
    return ''.join(result)


print(messageDecoder("Xlmw mw e wigvix qiwweki.", 4)) #should return "This is a secret message."
print(messageDecoder("Byffi Qilfx!", 20)) #should return "Hello World!"
print(messageDecoder("Zqd xnt njzx?", -1)) #should return "Are you okay?"
print(messageDecoder("oannLxmnLjvy", 9)) #should return "freeCodeCamp"