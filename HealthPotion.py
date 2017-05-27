import random

health = 50
difficulty = int(input())


if difficulty == 3:
    potion_health = int (random.randint(30,50) / difficulty)
    health = health + potion_health
    print(health)

elif difficulty == 2:
    potion_health = int (random.randint(20,50) / difficulty)
    health = health + potion_health
    print(health)

elif difficulty == 1:
    potion_health = int (random.randint(10,50) / difficulty)
    health = health + potion_health
    print(health)

else:
    print("Level not defined")
    print("Try a different level")