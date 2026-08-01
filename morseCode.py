'''
Given a Morse code string, return the decoded message using the following table:

Code	Letter	Code	Letter
.-	A	-.	N
-...	B	---	O
-.-.	C	.--.	P
-..	D	--.-	Q
.	E	.-.	R
..-.	F	...	S
--.	G	-	T
....	H	..-	U
..	I	...-	V
.---	J	.--	W
-.-	K	-..-	X
.-..	L	-.--	Y
--	M	--..	Z
Letters are separated by a single space
Words are separated by three spaces
'''

def decode_morse(code):

    morse = {
        ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
        "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
        "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
        ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
        "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
        "--..": "Z"
    }

    words = code.split("   ")
    decodedwords = []

    for word in words:
        letter = word.split(" ")
        decodedwords.append("".join(morse[l] for l in letter))

    return " ".join(decodedwords)

print(decode_morse("--..")) #should return "Z".
print(decode_morse("... --- ..."))# should return "SOS".
print(decode_morse("..-. .-. . . -.-. --- -.. . -.-. .- -- .--.")) # should return "FREECODECAMP".
print(decode_morse(".... . .-.. .-.. ---   .-- --- .-. .-.. -..")) #should return "HELLO WORLD".
print(decode_morse("- .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. . -..   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --.")) # should return "THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG".