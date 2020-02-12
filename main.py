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
points_data = list(points.items())
random.shuffle(points_data)

for key, value in points_data:
    print('{}: {}'.format(key, value))


""" Module-2: Input in a Session """


# Culprit calling method
def finding_culprit():
    return print('Finding...')
    # for key, value in points_data:
        # print(key, value)
        # if value == points[3]:
        #     print(value)
            # thief_detected = value
            # return print(thief_detected)


# Police calling method
def calling_police():
    print("POINT: {}, I'm Police. Finding the Thief...".format(points[2]))
    return finding_culprit()


# session
process = 0

while process < len(points_data):
    try:
        # main input
        input_1 = int(input('\nEnter a Number: '))

        # check garbage input
        if input_1 < 0:
            print('Enter a Positive Number.')
            continue

        # check input in data
        if input_1 in points:
            # check input is 'BOSS'
            if input_1 == 0:
                print("POINT: {}, I'm BOSS, Hey Police, Find the Thief...".format(points[input_1]))
                calling_police()






            # elif input_1 == 1:
            #     print('You Are ROBBER')
            # elif input_1 == 2:
            #     print('You Are POLICE')
            # else:
            #     print('You Are THIEF')

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

