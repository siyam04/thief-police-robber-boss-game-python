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
    police_input = int(input('\nHey Police, Find Who is Thief or Robber: '))

    if police_input in points:
        for key, value in points.items():
            if police_input == key:
                print('\nPolice Inputted: {} | Culprit ID: {}'.format(police_input, key))
                if points[key] == 90:
                    print('Robber Found! (POINT: {})'.format(points[key]))
                elif points[key] == 0:
                    print('Thief Found! (POINT: {})'.format(points[key]))


    # for key, value in points_data:
        # print(key, value)

    # if police_input in points:
    #     if police_input == points[police_input]:
    #         return print('ROBBER', police_input)
    #     elif police_input == points[police_input]:
    #         return print('THIEF', police_input)
        # if value[police_input] == points[1]:
        #     print('ROBBER', value[police_input])
        # elif value[police_input] == points[3]:
        #     print('THIEF', value[police_input])

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
                print("(POINT: {}) I'm BOSS, Hey Police, Find the Thief...".format(points[input_1]))
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

