""" Global Variables """
#game board
board = [
        "-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"
        ]

#list to save players name
players_name = []

#if game is still going
GAME_STILL_GOING = True

#someone wins the game, WINNER == ? player[0] or player[1] : None
WINNER = None
current_player = " "


""" function body """
#displaying the board 
def display_board():
    print(f'              {board[0]}|{board[1]}|{board[2]}')
    print(f'              {board[3]}|{board[4]}|{board[5]}')
    print(f'              {board[6]}|{board[7]}|{board[8]}')



def start_game():

    def intro():
        print("--------------------------------- Tick-Tack-Toe---------------------------------------------")
    
    #getting player name and adding it to player_name(list)
    def get_player_name():
        global current_player
        global players_name
        players = input("Enter player names: ")
        players_name = players.split(" ")
        current_player = players_name[0]

       
    #setting player position and player sign "X" or "O"
    def set_position(position):
        if current_player == players_name[0]:
            board[position] = "X"
        else:
            board[position] = "O"  
           


    #getting player game moves
    def handle_move():
        try:
            print(f'<{current_player}> turns....')
            position = int(input("Please choose a positon from 0-8: "))
            if board[position] != "-":
                print("spot has been filled already.....")
                handle_move()
            else:    
                set_position(position)
                display_board()
        except:
            print("Invalid Input....")
            handle_move()        


    def check_if_game_over():
        
        def check_row():
            global GAME_STILL_GOING, WINNER
            row1 = board[0] == board[1] == board[2] != "-" 
            row2 = board[3] == board[4] == board[5] != "-"  
            row3 = board[6] == board[7] == board[8] != "-" 
            if row1 or row2 or row3:
                WINNER = current_player
                GAME_STILL_GOING = False


        def check_column():
            global GAME_STILL_GOING, WINNER
            col1 = board[0] == board[3] == board[6] != "-" 
            col2 = board[1] == board[4] == board[7] != "-"  
            col3 = board[2] == board[5] == board[8] != "-" 
            if col1 or col2 or col3:
                WINNER = current_player
                GAME_STILL_GOING = False 
                

        def check_diagonal():
            global GAME_STILL_GOING, WINNER
            diagonal1 = board[0] == board[4] == board[8] != "-" 
            diagonal2 = board[2] == board[4] == board[6] != "-" 
            if diagonal1 or diagonal2:
                WINNER = current_player
                GAME_STILL_GOING = False 
                
                            

        def check_if_tie():
            global GAME_STILL_GOING
            """ filtering out the number of spots whose value is '-' """
            tie = list(filter(lambda x: x == "-", board))
            if len(tie) < 1:
                GAME_STILL_GOING = False 
            else:
                print(f"{len(tie)} spots available..")



        """ calling the above functions  """
        check_row()
        check_column()
        check_diagonal()
        check_if_tie()
  
    
    #changing the next player 
    def change_player():
        global current_player
        if current_player == players_name[0]:
           current_player = players_name[-1]
        else:
            current_player = players_name[0]

                
    """ function call """
    intro()
    get_player_name() 

    # display first phase of the game 
    display_board()

    while GAME_STILL_GOING:
        handle_move()
        #check if the game is over or not
        check_if_game_over()
        change_player()

    if WINNER == None:
        print("It's a tie.....") 
    else:    
        print(f'<{WINNER}> won the game....')
 
               


#starting the game.....
start_game()      