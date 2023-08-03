import random, time

# Create list of the board. This will be separated into three rows whenever outputed
board = ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']

# FUNCTIONS
# This displays the current game board
def displayBoard():
    for i in range(1,4):
        print(board[i * 3 - 3:3 * i])

# This asks the prompt of who will have the first turn
def gameStart():
    global cpuHadLastTurn, board
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    firstMove = input('Would you like to go first? (Y/N): ').lower()
    if firstMove == 'y':
        cpuHadLastTurn = True
    elif firstMove == "n":
        cpuHadLastTurn = False
    else: 
        print('Invalid Response.')
        return gameStart()

# This runs the turn for the player
def myTurn():
    global cpuHadLastTurn
    # select 1-9
    selection = int(input('Your Turn! Pick where to place your X by pressing a number between 1-9: '))
    # make sure it hasn't been picked
    if selection < 1 or selection > 9:
        print('Not a valid response. Try again.')
        return myTurn()
    if board[selection - 1] == 'X' or board[selection - 1] == 'O':
        print('Not a valid response. Try again.')
        return myTurn()
    # change and print list
    board[selection - 1] = 'X'
    cpuHadLastTurn = False
    
# This runs the turn for the computer
def cpuTurn():
    global cpuHadLastTurn
    selection = random.randint(1,9)
    if board[selection - 1] == 'X' or board[selection - 1] == 'O':
        return cpuTurn()
    print(f'The computer chose: {selection}')
    time.sleep(1)
    board[selection - 1] = 'O'
    cpuHadLastTurn = True

# This win check handles all 16 outcomes of a game (if I continued this project, I'd undoubtedly start here in optimizing it)
def winCheck():
    if board[0:3] == ['X', 'X', 'X']:
        displayBoard()
        print('You win!')
        playAgain()
    elif board[3:6] == ['X', 'X', 'X']:
        displayBoard()
        print('You win!')
        playAgain()
    elif board[6:9] == ['X', 'X', 'X']:
        displayBoard()
        print('You win!')
        playAgain()
    elif board[0:9:3] == ['X', 'X', 'X']:
        displayBoard()
        print('You win!')
        playAgain()
    elif board[1:9:3] == ['X', 'X', 'X']:
        displayBoard()
        print('You win!')
        playAgain()
    elif board[2:9:3] == ['X', 'X', 'X']:
        displayBoard()
        print('You win!')
        playAgain()
    elif board[0:9:4] == ['X', 'X', 'X']:
        displayBoard()
        print('You win!')
        playAgain()
    elif board[4:8:2] == ['X', 'X', 'X']:
        displayBoard()
        print('You win!')
        playAgain()
    elif board[0:3] == ['O', 'O', 'O']:
        displayBoard()
        print('You lose :(')
        playAgain()
    elif board[3:6] == ['O', 'O', 'O']:
        displayBoard()
        print('You lose :(')
        playAgain()
    elif board[6:9] == ['O', 'O', 'O']:
        displayBoard()
        print('You lose :(')
        playAgain()
    elif board[0:9:3] == ['O', 'O', 'O']:
        displayBoard()
        print('You lose :(')
        playAgain()
    elif board[1:9:3] == ['O', 'O', 'O']:
        displayBoard()
        print('You lose :(')
        playAgain()
    elif board[2:9:3] == ['O', 'O', 'O']:
        displayBoard()
        print('You lose :(')
        playAgain()
    elif board[0:9:4] == ['O', 'O', 'O']:
        displayBoard()
        print('You lose :(')
        playAgain()
    elif board[4:8:2] == ['O', 'O', 'O']:
        displayBoard()
        print('You lose :(')
        playAgain()
    elif (board[0] == 'X' or board[0] == 'O') and (board[1] == 'X' or board[1] == 'O') and (board[2] == 'X' or board[2] == 'O') and (board[3] == 'X' or board[3] == 'O') and (board[4] == 'X' or board[4] == 'O') and (board[5]== 'X' or board[5] == 'O') and (board[6] == 'X' or board[6] == 'O') and (board[7] == 'X' or board[7] == 'O') and (board[8] == 'X' or board[8] == 'O'):
        print("It's a tie! (or cat in tic-tac-toe-talk)")
        playAgain()

# This asks if the player would like to play another game
def playAgain():
    anotherRound = input('Would you like to play again? (Y/N): ').lower()
    if anotherRound == 'y':
        return gameStart()
    elif anotherRound == "n":
        print('Thanks for playing!')
        exit()
    else: 
        print('Invalid Response.')
        return playAgain()
# END OF FUNCTIONS


# Start of Program
print('Welcome to Tic-Tac-Toe!')
displayBoard()
gameStart()

# Loop through turns
for _ in range(30):
    displayBoard()
    if cpuHadLastTurn:
        myTurn()
        winCheck()
    displayBoard()
    time.sleep(2)
    cpuTurn()
    winCheck()


