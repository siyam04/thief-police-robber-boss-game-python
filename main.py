import random


""" Module-1: Randomly Shuffling """

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

# shuffling keys randomly
data = list(points.items())
random.shuffle(data)

for key, value in data:
    print('{}: {}'.format(key, value))
    # print('\n')


""" Module-2: Input in a Session """

# session
process = 0

while process < len(data):
    try:
        # main input
        input_1 = int(input('\nEnter a Number: '))

        # check garbage input
        if input_1 < 0:
            print('Enter a Positive Number.')
            continue

        # check 'BOSS'
        if input_1 in points:
            print(points[input_1])

    # check garbage input
    except ValueError:
        print('You Have to Write a Positive Integer; try again!')










# process = 3
# step = 1
#
# while process <= 3:
#     # for steps in range(step):
#         n = int(input('Enter an Integer: \n'))
#         if n <= 10:
#             for i in range(n):
#                 print(i)
#         else:
#             print(n,'is greater than 10')
#
#         print('Press', 0, 'for Stop')

