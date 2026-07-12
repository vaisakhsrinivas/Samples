'''
Given two star sign strings, return their compatibility percentage.

The signs are arranged in a wheel of 12 positions in this order: "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces",
wrapping back to "Aries" after "Pisces". Find the shortest distance between the two signs and return the compatibility:

Distance	Compatibility
0	"100%"
1	"40%"
2	"80%"
3	"30%"
4	"90%"
5	"20%"
6	"50%"
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
def horoscopeMatch():

    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    head = Node(signs[0])
    current = head
    for sign in signs[1:]:
        current.next = Node(sign)
        current = current.next
    current.next = head
    return head

def compatibility(str1, str2):
    matchpercentage = {0: "100%", 1: "40%", 2: "80%", 3: "30%", 4: "90%", 5: "20%", 6: "50%"}

    head = horoscopeMatch()
    current = head
    while current.value != str1:
        current = current.next
    start = current
    steps = 0
    while current.value != str2:
        current = current.next
        steps += 1
    mindis = min(steps, 12 - steps)
    return matchpercentage[mindis]

print(compatibility("Libra", "Sagittarius")) #should return "80%".
print(compatibility("Gemini", "Scorpio") )#should return "20%".
print(compatibility("Pisces", "Aries")) #should return "40%".
print(compatibility("Capricorn", "Cancer")) #should return "50%".
print(compatibility("Aquarius", "Aquarius")) #should return "100%".
print(compatibility("Virgo", "Taurus")) #should return "90%".
print(compatibility("Leo", "Scorpio")) #should return "30%".