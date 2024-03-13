import random

health = 50
difficulty = 1
potion = random.randint(25,50) / difficulty
print(health)
health = health + potion
print(int(health))
