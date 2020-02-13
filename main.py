import random


""" Module-1: Randomly Shuffling """

# Assigning initial values
boss = 100
robber = 90
police = 80
thief = 0

# Ordering characters
points = {
    0: boss,
    1: robber,
    2: police,
    3: thief
}

# Shuffling keys randomly
points_data = list(points.items())
random.shuffle(points_data)

for key, value in points_data:
    print('{}: {}'.format(key, value))


""" Module-2: Input in a Session """


# Police calling method
def calling_police():
    police_input = int(input("\nPOLICE: I'm finding who is THIEF: "))

    # Searching from random list
    for i, v in enumerate(points_data):
        if police_input == i:
            print('\npolice inputted: {} | culprit id: {}'.format(police_input, i))
            if points[i] == 90:
                print('*ROBBER found! (POINT: {})'.format(points[i]))
            elif points[i] == 0:
                print('*THIEF found! (POINT: {})'.format(points[i]))


# Session
process = 0

while process < len(points_data):
    try:
        # Main input
        print('\n---- GAME MENU ----')
        input_1 = int(input('\nenter a number: '))

        # Check garbage input
        if input_1 < 0:
            print('enter a positive number.')
            continue

        # Check input in data
        for i, v in enumerate(points_data):
            if input_1 == i:
                # Check input is BOSS or not
                if points[input_1] == 100:
                    print("\nBOSS: hey police, find the THIEF...")
                    calling_police()
                    # break

            # elif input_1 == 1:
            #     print('You Are ROBBER')
            # elif input_1 == 2:
            #     print('You Are POLICE')
            # else:
            #     print('You Are THIEF')

    # Check garbage input
    except ValueError:
        print("you've to write a positive integer; try again!")



