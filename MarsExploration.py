def MarsExploration(s):
    return sum(s[i] != "SOS"[i%3] for i in range(len(s)))


s = input()
message = MarsExploration(s)
print(message)