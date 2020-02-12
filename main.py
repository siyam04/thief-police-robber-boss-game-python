import random


# assigning initial values
boss = 100
robber = 90
police = 80
thief = 0

# ordering characters
points = {
    0: boss,
    1: robber,
    2: police,
    3: thief
}

# shuffling items
keys = list(points.keys())
random.shuffle(keys)

for key in keys:
    print(key)



