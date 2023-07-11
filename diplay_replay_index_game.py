game_list = [0, 1, 2]

def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)

display_game(game_list)

def position_choice():
    choice = "wrong"

    while choice not in ['0', '1', '2']:

        choice = input("Pick a position (0,1,2): ")

        if choice not in ['0', '1', '2']:
            print("Sorry, invalid choice!")

    return int(choice)


position = position_choice()
print(position)

def replacement_value(game_list, Position):

    user_placement = input("Type a string to place at position: ")
    game_list[Position] = user_placement
    return game_list

replace = replacement_value(game_list, 1)
print(replace)

'''
def gameon_choice():
    choice = "wrong"

    while choice not in ['Y','N']:

        choice = input("Keep playing? (Y or N) ")

        if choice not in ['Y','N']:
            print("Sorry, I dont understand, please choose Y or N")

    if choice == "Y":
        return True
    else:
        return False


game = gameon_choice()
print(game)

game_on = True
game_list = [0,1,2]

while game_on:
    display_game(game_list)

    place = position
    game_list = replacement_value(game_list, position)
    display_game(game_list)
    game_on = gameon_choice()
    '''

