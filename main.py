import random


""" Module-1: Randomly Shuffling """

# Shuffling indexes randomly
points = [100, 80, 60, 0]
random.shuffle(points)

for i, v in enumerate(points):
    print('{}: {}'.format(i, v))


""" Module-3: Finding Thief, Summation Methods """


# Police calling method

def calc_points():
    pass


def calling_police():
    # Detecting Thief
    temp_points = [e for e in points if e not in (100, 80)]
    random.shuffle(temp_points)

    print(temp_points)
    if temp_points[0] == 0:
        print('\nPOLICE: Success! THIEF Found, ')
        print('sum()')
    else:
        print('\nPOLICE: Not Found')


""" Module-2: Input in a Session """

# Session
process = 0

while process < len(points):
    try:
        # Main input
        print('\n---- GAME MENU ----')
        input_1 = int(input('\nenter a number: '))

        # Check garbage input
        if input_1 < 0:
            print('enter a positive number.')
            continue

        if input_1 > len(points):
            print('index not in list')
            continue

        # Check input in data
        for i, v in enumerate(points):
            if input_1 == i:
                # Check input is BOSS or not
                if points[input_1] == 100:

                    print("\nBOSS: hey police, which number is thief?")
                    calling_police()
                    # break

                elif points[input_1] == 80:
                    print('I am POLICE')

                elif points[input_1] == 60:
                    print('ROBBER point')

                elif points[input_1] == 0:
                    print('THIEF point')

    # Check garbage input
    except ValueError:
        print("you've to write a positive integer; try again!")



