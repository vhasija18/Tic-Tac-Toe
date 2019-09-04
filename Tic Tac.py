play_board = ["-", "-", "-","-", "-", "-","-", "-", "-"]

current_player = "X"
winner = None
game_is_on = True
def display_board():
    print(play_board[0]+"|"+play_board[1]+"|"+play_board[2])
    print(play_board[3]+"|"+play_board[4]+"|"+play_board[5])
    print(play_board[6]+"|"+play_board[7]+"|"+play_board[8])
    return


def play_game():
    #Display the board
    display_board()
    
    while game_is_on:
        print("ssds")
        handle_turn(current_player)
        check_status()
        flip_player()
        
    if winner =="X" or winner =="O":
        print("Winner is:" + winner)
    elif winner == None:
        print("Tie")

def handle_turn(player):
    print(player + "'s turn.")
    valid = False
    while  valid == False:
        position = input("Enter the position from 1 to 9 ")
        position  = int(position)-1
        if position>=0 and position<=8:
            valid = True
            if play_board[position] == '-':
                valid = True
            else:
                valid = False
                print("Try again ")
        else:
            valid = False
            print("Try Again" )
            
        
    play_board[position] = player
    display_board()
    return

def check_status():
    check_winner()
    check_tie()

def check_tie():
    global game_is_on 
    if "-" not in play_board:
        game_is_on = False
        return True
    else:
        return False

def check_winner():
    global winner
    row_winner = row_win()
    column_winner = column_win()
    diagonal_winner = diagonal_win()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner

def row_win():
    global game_is_on
    row1 = play_board[0]==play_board[1]== play_board[2]!='-'
    row2 = play_board[3]==play_board[4]== play_board[5]!='-'
    row3 = play_board[6]==play_board[7]== play_board[8]!='-'
    
    if row1 or row2 or row3 :
        game_is_on = False
    
    if row1:
        return play_board[0]
    elif row2:
        return play_board[3]
    elif row3:
        return play_board[6]
 
def column_win():
       global game_is_on
       column1 = play_board[0]== play_board[3]== play_board[6]!='-'
       column2 = play_board[1]== play_board[4]== play_board[7]!='-'
       column3 = play_board[2]== play_board[5]== play_board[8]!='-'
       
       if column1 or column2 or column3:
           game_is_on = False
    
       if column1:
           return play_board[0]
       elif column2: 
           return play_board[1]
       elif column3:
           return play_board[2]

def diagonal_win():
    global game_is_on
    diagonal1 = play_board[0]==play_board[4]==play_board[8]!='-'
    diagonal2 = play_board[6]==play_board[4]==play_board[2]!='-'
    
    if diagonal1 or diagonal2:
        game_is_on = False
    
    if diagonal1:
        return play_board[0]
    elif diagonal2:
        return play_board[6]

def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
    return

play_game()