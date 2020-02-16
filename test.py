# Create the Board
board_dictionary = [" ", " ", " ",
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
        print_board(board_dictionary)
        # Take in user input
        userInput = 0
        while True:
            try:
                userInput = int(input("\nInput a location that you would like to mark (1-9): "));
            except ValueError:
                print("\nPlease type an integer.")
            if userInput in range(1, 10):
                break
        # Change marker point if valid
        if board_dictionary[userInput - 1] == " ":
            board_dictionary[userInput - 1] = mark
            break
        else:
            print("\nThat space is already taken.")


