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

    # Searching from dictionary
    # if police_input in points:
    #     for key, value in points.items():
    #         if police_input == key:
    #             print('\npolice inputted: {} | culprit id: {}'.format(police_input, key))
    #             if points[key] == 90:
    #                 print('*ROBBER found! (POINT: {})'.format(points[key]))
    #             elif points[key] == 0:
    #                 print('*THIEF found! (POINT: {})'.format(points[key]))

    # for i in points:
    #     if police_input == i:
    #         print('\npolice inputted: {} | culprit id: {}'.format(police_input, i))
    #         if points[i] == robber:
    #             print('*ROBBER found! (POINT: {})'.format(points[i]))
    #         elif points[i] == thief:
    #             print('*THIEF found! (POINT: {})'.format(points[i]))

    # Searching from random list
    # for i, v in enumerate(points):
    #     if police_input == i:
    #         print('\npolice inputted: {} | culprit id: {}'.format(police_input, i))
    #         if points[i] == 90:
    #             print('*ROBBER found! (POINT: {})'.format(points[i]))
    #         elif points[i] == 0:
    #             print('*THIEF found! (POINT: {})'.format(points[i]))


# Session
process = 0

while process < len(points_data):
    try:
        # main input
        print('\n---- GAME MENU ----')
        input_1 = int(input('\nenter a number: '))

        # check garbage input
        if input_1 < 0:
            print('enter a positive number.')
            continue

        # check input in data
        if input_1 in points:
            # check input is 'BOSS'
            if input_1 == 0:
                print("\nBOSS: hey police, find the THIEF...".format(points[input_1]))
                calling_police()
                # break

            # elif input_1 == 1:
            #     print('You Are ROBBER')
            # elif input_1 == 2:
            #     print('You Are POLICE')
            # else:
            #     print('You Are THIEF')

    # check garbage input
    except ValueError:
        print("you've to write a positive integer; try again!")



