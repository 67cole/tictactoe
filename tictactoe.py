'''
Creating a tic tac toe game as a project from scratch
Meant to be a terminal based game with two local players!
'''

# Establish global variables
board = ['-', '-', '-',
        '-', '-', '-',
        '-', '-', '-']

gameStatus = True
gameTick = 0

# Introduce the game + some more global variables
print("Welcome to Tic Tac Toe - a two-player terminal based game!")
p1 = input("Please enter Player 1's name: ")
currentPlayer = input("Welcome " + p1 + "! Please pick out of the two symbols: 'X' or 'O' ")

# Error case: Incorrect input
while currentPlayer != 'X' and currentPlayer != 'O':
    currentPlayer = input("You have picked an invalid symbol. Please try again between 'X' and 'O' ") 

p2 = input("Then Player 2 is 'O'! What is Player 2's name? ")
print("Welcome " + p2 + "! Let's start Tic Tac Toe :)")
print("The rules are simple, please indicate a number from 0 - 8 inclusive of what position to play. The numbers are in horizontal order of board positions.")
print("Let's start!")

# Functions
def printBoard():

    # print in rows and columns
    print(board[0] + " | " + board[1] + " | " + board[2])

    # column
    print("-" * 9)

    # remaining
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])

# Grabs player input
def playerInput():

    global board
    
    # gameTick are used to indicate who's turn it is
    # Game always starts with Player 1 first!

    # Grab input from whatever player
    if gameTick % 2 == 0:
        placement = input(p1 + "'s turn. Please enter a position: ")
    else:
        placement = input(p2 + "'s turn. Please enter a position: ")
    
    # Error case: input isn't a number, isn't from 0 - 8 or board position taken already
    while placement.isnumeric() is False or int(placement) < 0 or int(placement) > 8 or (board[int(placement)] != '-'):
        placement = input("Invalid input. Please try again. ")
    
    placement = int(placement)

    # Place on board
    board[placement] = currentPlayer


# Checks win condition
def checkWin():

    winner = False

    # row check
    if (board[0] == board[1] == board[2] and board[0] != "-") or (board[3] == board[4] == board[5] and board[3] != "-") or (board[6] == board[7] == board[8] and board[6] != "-"):
        winner = True
    
    # column check
    if (board[0] == board[3] == board[6] and board[0] != "-") or (board[1] == board[4] == board[7] and board[1] != "-") or (board[2] == board[5] == board[8] and board[2] != "-"):
        winner = True
    
    # diagonal
    if (board[0] == board[4] == board[8] and board[0] != "-") or (board[2] == board[4] == board[6] and board[2] != "-"):
        winner = True
    
    return winner

# Announces winner
def announceWinner():

    # print board first
    printBoard()

    # check who won using gameTick
    if gameTick % 2 == 0:
        print(p1 + " has won!")
    
    else:
        print(p2 + " has won!")


# Checks tie condition
def checkTie():
    
    # if '-' isn't on the board, then the game is a tie
    if '-' not in board:
        printBoard()
        print("It's a tie!")

        return True
    
    return False



# Switches the player
def switchPlayer():

    # Increase the gameTick
    global gameTick
    gameTick += 1

    # Switch current player
    global currentPlayer
    if currentPlayer == 'O':
        currentPlayer = 'X'
    else:
        currentPlayer = 'O'
    


# Main body
while gameStatus:

    # print board
    printBoard()

    # grab input
    playerInput()
    
    # checks win
    if checkWin() is True:
        announceWinner()
        break
    
    # checks tie
    if checkTie() is True:
        break

    switchPlayer()


