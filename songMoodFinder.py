'''
Given a genre string and a BPM number for a song, determine the mood using the following table:

Mood	Genre	BPM Range
"focus"	"classical"	60–109
"focus"	"electronic"	60–89
"happy"	"pop"	60–180
"happy"	"classical"	110–180
"happy"	"rock"	60–129
"happy"	"electronic"	90–134
"hype"	"rock"	130–180
"hype"	"electronic"	135–180

'''

def get_mood(genre, bpm):

    mood = {
        ("focus", "classical") : (60, 109),
        ("focus", "electronic"): (60, 89),
        ("happy", "rock") : (60, 129),
        ("happy", "electronic"): (90, 134),
        ("happy", "classical"): (110, 180),
        ("happy", "pop"): (60, 180),
        ("hype", "rock"): (130, 180),
        ("hype", "electronic"): (135, 180),
    }

    for (m,g),(low,high) in mood.items():
        if genre == g and low <= bpm <= high:
            return m
    return None


print(get_mood("rock", 111)) # should return "happy".
print(get_mood("electronic", 74)) # should return "focus".
print(get_mood("classical", 180)) # should return "happy".
print(get_mood("rock", 155)) #should return "hype".
print(get_mood("electronic", 90)) #should return "happy".
print(get_mood("classical", 67)) #should return "focus".
print(get_mood("pop", 100)) #should return "happy".
print(get_mood("electronic", 135)) #should return "hype".