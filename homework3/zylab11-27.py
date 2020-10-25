# Basim Siddiqui
# PSID: 1517778

team_dictionary = {}
i = 1
for i in range(1, 6):
    jersey_num = int(input("Enter player {}'s jersey number:\n".format(i)))
    rating = int(input("Enter player {}'s rating:\n".format(i)))
    print()
    if jersey_num > 99 and jersey_num < 0 and rating > 9 and rating < 0:
        print("Invalid entry")
        break
    else:
        team_dictionary[jersey_num] = rating

print('ROSTER')
for jersey_num, rating in sorted(team_dictionary.items()):
    print("Jersey number: %d, Rating: %d" % (jersey_num, rating))

menu = ''
while menu != 'q':
    print('\nMENU\n'
          'a - Add player\n'
          'd - Remove player\n'
          'u - Update player rating\n'
          'r - Output players above a rating\n'
          'o - Output roster\n'
          'q - Quit\n')
    menu = input('Choose an option:\n')

    if menu == 'a':
        jersey_num = int(input("Enter a new player's jersey number:\n".format(i)))
        rating = int(input("Enter the player's rating:\n".format(i)))
        team_dictionary[jersey_num] = rating

    elif menu == 'd':
        jersey_num = int(input("Enter a jersey number:\n"))
        if jersey_num in team_dictionary.keys():
            del team_dictionary[jersey_num]

    elif menu == 'u':
        jersey_num = int(input("Enter a jersey number:\n"))
        if jersey_num in team_dictionary.keys():
            rating = int(input("Enter a new rating for player:\n"))
            team_dictionary[jersey_num] = rating

    elif menu == 'r':
        rating_parameter = int(input("Enter a rating:\n"))
        print('ABOVE {}'.format(rating_parameter))
        for jersey_num, rating in sorted(team_dictionary.items()):
            if rating > rating_parameter:
                print("Jersey number: %d, Rating: %d" % (jersey_num, rating))

    elif menu == 'o':
        print("ROSTER")
        for jersey_num, rating in sorted(team_dictionary.items()):
            print("Jersey number: %d, Rating: %d" % (jersey_num, rating))

