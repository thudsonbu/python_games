def main():
    # get player markers
    markers = intro_get_markers()
    player1_mark = markers[0]
    player2_mark = markers[1]

    # start playing the game
    game = True
    while(game):
        # create game board
        board = [" ", " ", " ",
                 " ", " ", " ",
                 " ", " ", " "]

        # loopes through player turns until win or board full
        game_loop(board,player1_mark,player2_mark)

        # querry keep playing
        while(True):
            keep_playing = input("\nWould you like to play again? (Y/N)")
            if keep_playing.upper() == "Y":
                game = True
                break
            elif keep_playing.upper() == "N":
                game = False
                break
            else:
                print("Invalid Input")
    # bye
    print("\nThanks for playing!")

 # prints the game board
def print_board(dictionary):
    print("\nBoard Display: \n")
    # print first line of board
    print("| ", end="")
    for i in range(0, 3):
        print(dictionary[i], end=" | ")
    print("")
    print("| ", end="")
    # print second line of board
    for i in range(3, 6):
        print(dictionary[i], end=" | ")
    print("")
    print("| ", end="")
    # print third line of board
    for i in range(6, 9):
        print(dictionary[i], end=" | ")
    print()

# a player turn for marking board
def player_turn(game_board,mark):
    print("\nPlayer " + mark + "'s turn.")
    while True:
        print_board(game_board)
        # Take in user input
        user_input = 0
        while True:
            try:
                user_input = int(input("\nInput a location that you would like to mark (1-9): "))
            except ValueError:
                print("\nPlease type an integer.")
            if user_input in range(1, 10):
                break
        # Change marker point if valid
        if game_board[user_input - 1] == " ":
            game_board[user_input - 1] = mark
            break
        else:
            print("\nThat space is already taken.")

# checks a game board if win found for specific mark
def check_win(game_board, mark):
    # combinations of marks that cause a win
    win_combinations = [[1, 2, 3],
                        [4, 5, 6],
                        [7, 8, 9],
                        [1, 4, 7],
                        [2, 5, 8],
                        [3, 6, 9],
                        [1, 5, 9],
                        [3, 5, 7]]
    # Mark list to hold all players marked locations
    mark_list = []
    # Add players marked locations to marked list
    for i in range(0, len(game_board)):
        if game_board[i] == mark:
            mark_list.append(i + 1)
    # Check if win combination in mark list
    combination_found = False
    for combination in win_combinations:  # Iterate through combinations
        count = 0  # Counts how many matches in combination
        for i in combination:
            if i in mark_list:
                count += 1
        if count == 3:  # If there are three matches a combination has been found
            combination_found = True
    return combination_found

# introduction to the game that returns player's chosen markers
def intro_get_markers():
    print("\nWelcome to Tom's Tic Tac Toe.")
    while True:
        try:
            player1_mark = str(input("\nWhat will player1's market be? "))
            break
        except ValueError:
            print("\nInvalid input, must be a character.")
    print("\nPlayer1's marker is " + player1_mark)
    while True:
        try:
            player2_mark = str(input("\nWhat will player2's marker be? "))
            break
        except ValueError:
            print("\nInvalid input, must be a character.")
    print("\nPlayer2's marker is " + player2_mark)
    return player1_mark, player2_mark

# loops through player turns until win or board it full (tie)
def game_loop(game_board,player1_mark,player2_mark):
    round = 1
    while(True):
        player_turn(game_board,player1_mark)
        if check_win(game_board,player1_mark):
            print("\n!!! PLAYER1 WINS !!!")
            print_board(game_board)
            break
        round += 1
        if round > 9: # check is in the middle since last round is round 9 (odd)
            print("\n!!! TIE !!!")
            print_board(game_board)
            break
        player_turn(game_board,player2_mark)
        if check_win(game_board,player2_mark):
            print("\n!!! PLAYER2 WINS !!!")
            print_board(game_board)
            break
        round += 1


if __name__ == '__main__':
    main()
