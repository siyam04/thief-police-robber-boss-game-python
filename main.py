import random


""" Module-1: Randomly Shuffling """

# Shuffling indexes randomly
points = [100, 80, 60, 0]
random.shuffle(points)

for i, v in enumerate(points):
    print('{}: {}'.format(i, v))


""" Module-3: Finding Thief """


# Police calling method
def calling_police():
    robber = points.index(60)
    thief = points.index(0)

    print('{}'.format(robber))
    print('{}'.format(thief))

    # Sometimes Detecting Thieves (BUG)
    # for i in points:
    #     if i == thief:
    #         print('\nSuccess! THIEF is number {}'.format(i))
    #     else:
    #         print('Not Found!')

    # Always Detecting Thieves
    for i, v in enumerate(points):
        if i == thief:
            print('\nSuccess! THIEF is number {}'.format(i))


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

    # Check garbage input
    except ValueError:
        print("you've to write a positive integer; try again!")



