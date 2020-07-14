from IPython.display import clear_output

def display_board(board):
    clear_output()
    print(board[7]+' | '+board[8]+' | '+board[9])
    print("----------" )
    print(board[4]+' | '+board[5]+' | '+board[6])
    print("----------" )
    print(board[1]+' | '+board[2]+' | '+board[3])
############################################################    
def player_input():
    choice = ' '
    while choice != 'X' or choice !='O':
        choice = input('Enter player1 marker (X or O):').upper()
        if choice == 'X':
            return ('X','O')
        else:
            return ('O','X')
##################################################################
def place_marker(board, marker, position):
    if marker.upper() not in ['X','O']:
        return print("Inavlid marker")
    if position not in range(1,10):
        return print("Inavlid position, please try again")

    board[position] = marker.upper()
    return board
######################################################################    
def win_check(board, mark):
    #need to check all rows
    #all columns
    #2 diagonals
    return ((board[7]==board[8]==board[9]==mark)or
           (board[4]==board[5]==board[6]==mark)or
           (board[1]==board[2]==board[3]==mark)or
           (board[7]==board[4]==board[1]==mark)or
           (board[9]==board[6]==board[3]==mark)or
           (board[8]==board[5]==board[2]==mark)or
           (board[1]==board[5]==board[9]==mark)or
           (board[7]==board[5]==board[3]==mark))
#########################################################           
import random

def choose_first():
    first = random.randint(1,2)
    if first==1:
        return "player1"
    else:
        return "player2"
#################################################
def space_check(board, position):
    return board[position]==' '
##################################################
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
################################################## 
def player_choice(board):
    opt=0

    while opt not in range(1,10) or not space_check(board,opt):
        opt = int(input("Choose a number (1-9):"))
        
    return opt
############################################################
def replay():
    again = 's'
    while again.upper() != 'Y' or again.upper != 'N':
        again = input("Do you want to play again (Y or N):").upper()
        if again == 'Y':
            return True
        elif again =='N':
            return False
###############################################################
print('Welcome to Tic Tac Toe!')
play_again = True

while play_again:
    
    board = [' ']*10

    #selecting player's markers
    player1_marker,player2_marker = player_input()
    
   # print("player1's Marker = {}".format(player1))
   # print("player2's Marker = {}".format(player2))
    
    #who will start the game
    turn = choose_first()
    print(turn + ' will go first')
    # Set the game up here
    play_game = input("Ready to play? Y or N?")
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        #player1's turn
        if turn == "player1":
            #display the board
            display_board(board)
            #choose the position of marker
            position = player_choice(board)
            #place the marker
            place_marker(board,player1,position)
            #check if won
            if win_check(board,player1):
                display_board(board)
                print("Congratulations! player1 has won")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("It's a tie!!")
                    game_on = False
                else:
                    turn = "player2"
            
        else:
        # Player2's turn.
            display_board(board)
            #choose the position of marker
            position = player_choice(board)
            #place the marker
            place_marker(board,player2,position)
            #check if won
            if win_check(board,player2):
                display_board(board)
                print("Congratulations! player2 has won")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("It's a tie!!")
                    game_on = False
                else:
                    turn = 'player1'    
    if not replay():
        break

