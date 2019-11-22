theBoard = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}
player = "X"


# this function prints the board
def printBoard(board):
    print(board["1"] + '|' + board["2"] + '|' + board["3"])
    print('-+-+-')
    print(board["4"] + '|' + board["5"] + '|' + board["6"])
    print('-+-+-')
    print(board["7"] + '|' + board["8"] + '|' + board["9"])


# flips the player
def changePlayer():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"


# returns True if a player has won
def checkVictory():
    victory = False
    if theBoard["1"] == theBoard["2"] == theBoard["3"] != " ":
        victory = True
    elif theBoard["4"] == theBoard["5"] == theBoard["6"] != " ":
        victory = True
    elif theBoard["7"] == theBoard["8"] == theBoard["9"] != " ":
        victory = True
    elif theBoard["1"] == theBoard["4"] == theBoard["7"] != " ":
        victory = True
    elif theBoard["2"] == theBoard["5"] == theBoard["8"] != " ":
        victory = True
    elif theBoard["3"] == theBoard["6"] == theBoard["9"] != " ":
        victory = True
    elif theBoard["1"] == theBoard["5"] == theBoard["9"] != " ":
        victory = True
    elif theBoard["3"] == theBoard["5"] == theBoard["7"] != " ":
        victory = True
    return victory


# calls the function that prints the board
printBoard(theBoard)

# variable to track the active player position
i = 0

# this loop runs till the whole board is filled
while i < 9:
    print('Enter block number')
    choice = input()
    if theBoard[choice] == " ":
        theBoard[choice] = player
        i += 1
        if checkVictory():
            print("Player " + player + " has won!")
            break
        changePlayer()
        printBoard(theBoard)
    else:
        print("Invalid Block! Enter another value")
    if i == 9 and not checkVictory():
        print("It's a draw! Better luck next time.")
