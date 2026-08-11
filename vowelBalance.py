'''
Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

The string can contain any characters.
The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
If there's an odd number of characters in the string, ignore the center character.
'''

def is_balanced(string):

    def count_vowels(string):
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        count = 0
        for char in string:
            if char in vowels:
                count += 1
        return count

    length = len(string)
    mid = length//2
    if length%2 != 0:
        fhalf = count_vowels(string[:mid])
        shalf = count_vowels(string[mid+1:])
    else:
        fhalf = count_vowels(string[:mid])
        shalf = count_vowels(string[mid:])
    return fhalf == shalf


print(is_balanced("racecar")) #should return True.
print(is_balanced("Lorem Ipsum")) #should return True.
print(is_balanced("Kitty Ipsum")) #should return False.
print(is_balanced("string")) #should return False.
print(is_balanced(" ")) #should return True.
print(is_balanced("abcdefghijklmnopqrstuvwxyz")) #should return False.
print(is_balanced("123A#b!E&*456-o.U")) #should return True.