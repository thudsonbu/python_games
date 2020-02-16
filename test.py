# Create the Board
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


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


def player_turn(mark):
    while True:
        print_board(board)
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
        if board[user_input - 1] == " ":
            board[user_input - 1] = mark
            break
        else:
            print("\nThat space is already taken.")


def check_win(game_board, mark):
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

print(check_win(board,"X"))

