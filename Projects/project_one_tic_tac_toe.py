import os

#Clear everything shown in terminal before the game starts.
os.system('cls||clear')
game_running = True

theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)


#Asks first user to pick a letter and verifies response is either "x" or "o"
def get_valid_choice(valid_choices):
    while True:
        current_player = input('Please enter "x" or "o" to select your letter:  ').lower()
        if current_player in valid_choices:
            return current_player
        else:
          print("\nPlease type in a valid response")

            
def printBoard(board):
    print("Your board:       Reference locations:")
    print(board['1'] + '|' + board['2'] + '|' + board['3'] + '             1|2|3' + "\n" + '-+-+-             -+-+-' + "\n" +
          board['4'] + '|' + board['5'] + '|' + board['6'] + '             4|5|6' + "\n" + '-+-+-             -+-+-' + "\n" +
          board['7'] + '|' + board['8'] + '|' + board['9'] + '             7|8|9'                                           )


def game():
    global game_running

    current_player = get_valid_choice(["x", "o"])
    count = 0


    while game_running:
        printBoard(theBoard)
        print("\n" + current_player + "'s turn.")
        position = input("Choose a spot on the board (1-9): ")
        print("\n")

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a spot on the board (1-9): ")   

        if theBoard[position] == ' ':
            theBoard[position] = current_player
            count += 1
        else:
            print("That spot on the board has already been claimed, please choose a new one.")
            continue

        #Checks for win after 5 rounds (the quickest possible game)
        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nPlayer " + current_player + " has won!")
                play_again()
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("\nPlayer " + current_player + " has won!")
                play_again()
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nPlayer " + current_player + " has won!")
                play_again()
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                printBoard(theBoard)
                print("\nPlayer " + current_player + " has won!")
                play_again()
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                printBoard(theBoard)
                print("\nPlayer " + current_player + " has won!")
                play_again()
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nPlayer " + current_player + " has won!")
                play_again()
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                printBoard(theBoard)
                print("\nPlayer " + current_player + " has won!")
                play_again()
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':
                printBoard(theBoard)
                print("\nPlayer " + current_player + " has won!")
                play_again()

        if count == 9:
            printBoard(theBoard)
            print("\nIt's a Tie!\n")
            play_again()
            

        # Now we have to change the player after every move.
        if current_player == "x":
            current_player = "o"
        elif current_player == "o":
            current_player = "x"

def play_again():
    global game_running

    restart = input('Would you like to play again? Type "Yes" to continue, otherwise enter any other key to end: ').lower()
    if restart == "yes":
        for key in board_keys:
            theBoard[key] = " "
        game()
    elif restart != "yes":
        game_running = False
game()