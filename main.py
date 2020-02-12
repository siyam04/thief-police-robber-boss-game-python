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
items = list(points.items())
random.shuffle(items)

for key, value in items:
    print('{}: {}'.format(key, value))
    # print('\n')


""" Module-2: Input in a Session """

# session
process = 4

while process <= 4:
    try:
        input_1 = int(input('\nEnter a Number: '))

        if input_1 < 0:
            print('Enter a Positive Number.')
            continue

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

