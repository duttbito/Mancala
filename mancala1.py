BLOCK_WIDTH = 6
BLOCK_HEIGHT = 5
BLOCK_SEP = "*"
SPACE = ' '

def draw_board(top_cups, bottom_cups, mancala_a, mancala_b):
    """
    draw_board is the function that you should call in order to draw the board.
        top_cups and bottom_cups are lists of strings.  Each string should be length BLOCK_WIDTH and each list should be of length BLOCK_HEIGHT.
        mancala_a and mancala_b should be 2d lists of strings.  Each string should be BLOCK_WIDTH in length, and each list should be 2 * BLOCK_HEIGHT + 1

    :param top_cups: This should be a list of strings that represents cups 1 to 6 (Each list should be at least BLOCK_HEIGHT in length, since each string in\
 the list is a line.)
    :param bottom_cups: This should be a list of strings that represents cups 8 to 13 (Each list should be at least BLOCK_HEIGHT in length, since each strin\
g in the list is a line.)
    :param mancala_a: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala at position 7.
    :param mancala_b: This should be a list of 2 * BLOCK_HEIGHT + 1 in length which represents the mancala at position 0.
    """
    board = [[SPACE for _ in range((BLOCK_WIDTH + 1) * (len(top_cups) + 2) + 1)] for _ in range(BLOCK_HEIGHT * 2 + 3)]
    for p in range(len(board)):
        board[p][0] = BLOCK_SEP
        board[p][len(board[0]) - 1] = BLOCK_SEP

    for q in range(len(board[0])):
        board[0][q] = BLOCK_SEP
        board[len(board) - 1][q] = BLOCK_SEP

    # draw midline
    for p in range(BLOCK_WIDTH + 1, (BLOCK_WIDTH + 1) * (len(top_cups) + 1) + 1):
        board[BLOCK_HEIGHT + 1][p] = BLOCK_SEP

    for i in range(len(top_cups)):
        for p in range(len(board)):
            board[p][(1 + i) * (1 + BLOCK_WIDTH)] = BLOCK_SEP
    for p in range(len(board)):
        board[p][1 + BLOCK_WIDTH] = BLOCK_SEP
        board[p][len(board[0]) - BLOCK_WIDTH - 2] = BLOCK_SEP

    for i in range(len(top_cups)):
        draw_block(board, i, 0, top_cups[i])
        draw_block(board, i, 1, bottom_cups[i])

    draw_mancala(0, mancala_a, board)
    draw_mancala(1, mancala_b, board)

    print('\n'.join([''.join(board[i]) for i in range(len(board))]))


def draw_mancala(fore_or_aft, mancala_data, the_board):
    """
        Draw_mancala is a helper function for the draw_board function.
    :param fore_or_aft: front or back (0, or 1)
    :param mancala_data: a list of strings of length 2 * BLOCK_HEIGHT + 1 each string of length BLOCK_WIDTH
    :param the_board: a 2d-list of characters which we are creating to print the board.
    """
    if fore_or_aft == 0:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][1 + j] = data[j]
    else:
        for i in range(len(mancala_data)):
            data = mancala_data[i][0: BLOCK_WIDTH].rjust(BLOCK_WIDTH)
            for j in range(len(mancala_data[0])):
                the_board[1 + i][len(the_board[0]) - BLOCK_WIDTH - 1 + j] = data[j]


def draw_block(the_board, pos_x, pos_y, block_data):
    """
        Draw block is a helper function for the draw_board function.
    :param the_board: the board is the 2d grid of characters we're filling in
    :param pos_x: which cup it is
    :param pos_y: upper or lower
    :param block_data: the list of strings to put into the block.
    """
    for i in range(BLOCK_HEIGHT):
        data = block_data[i][0:BLOCK_WIDTH].rjust(BLOCK_WIDTH)
        for j in range(BLOCK_WIDTH):
            the_board[1 + pos_y * (BLOCK_HEIGHT + 1) + i][1 + (pos_x + 1) * (BLOCK_WIDTH + 1) + j] = data[j]

#function to get the players name
def get_player(player_num):
    
    player = input("Player " + player_num + " please tell me your name: ")
    
    return player

#function for taking turns 
def take_turn(player, game_cups, top_cups, bottom_cups, mancala_a, mancala_b):
    is_last_stone_in_mancala = True
    while is_last_stone_in_mancala:
        is_last_stone_in_mancala = False
        cup_num = int(input(player + " What cup do you want to move? "))

        #check if the player picks either mancalas which is not allowed
        while cup_num == 0 or cup_num == 7:
            print("You cannot pick from the mancalas")
            cup_num = int(input(player + " What cup do you want to move? "))    
        
        #check if the player picked an empty cup
        while game_cups[cup_num] == 0:
            print("The cup you picked is empty")
            cup_num = int(input(player + " What cup do you want to move? "))    
        
        #the logic behind each move 
        next = 1
        while game_cups[cup_num] > 0:
            game_cups[cup_num] = game_cups[cup_num] - 1
            
            if cup_num == 13:
                next = -cup_num
            
            game_cups[cup_num + next] = game_cups[cup_num + next] + 1
            
            if game_cups[cup_num] == 0:
                if cup_num + next == 0 or cup_num + next == 7:
                    is_last_stone_in_mancala = True
                    print("Your last stone landed in a mancala.")
                    print("Go again please...")
                else:
                    False

            if cup_num + next == 13:
                next = -cup_num
            else:
                next = next + 1
        
        #inserts the mancala list into the board
        mancala_b[8] = str(game_cups[7])
        mancala_a[8] = str(game_cups[0])
        
        top_cups[0][3] = str(game_cups[1])
        top_cups[1][3] = str(game_cups[2])
        top_cups[2][3] = str(game_cups[3])
        top_cups[3][3] = str(game_cups[4])
        top_cups[4][3] = str(game_cups[5])
        top_cups[5][3] = str(game_cups[6])
        
        bottom_cups[0][3] = str(game_cups[13])
        bottom_cups[1][3] = str(game_cups[12])
        bottom_cups[2][3] = str(game_cups[11])
        bottom_cups[3][3] = str(game_cups[10])
        bottom_cups[4][3] = str(game_cups[9])
        bottom_cups[5][3] = str(game_cups[8])
        
        if is_game_over(game_cups):
            is_last_stone_in_mancala = False

        
        draw_board(top_cups, bottom_cups, mancala_a, mancala_b)    

#function to check if the game has ended        
def is_game_over(cups_list):
    #check if top cups is empty
    is_row1_empty = True
    for i in range(1, 7):
        if cups_list[i] != 0:
            is_row1_empty = False

    #check if bottom cups is empty
    is_row2_empty = True
    for i in range(8, 14):
        if cups_list[i] != 0:
            is_row2_empty = False
    
    if is_row1_empty or is_row2_empty:
        return True
    else:
        return False

#function to check which player won or if they tied   
def win_game(winner_list, player_1, player_2):
    #check if player 2 won
    if winner_list[0] > winner_list[7]:
        print(player_2 + " is the winner")
    #check if player 1 won
    elif winner_list[7] > winner_list[0]:
        print(player_1 + " is the winner")
    #check for a tie
    elif winner_list[7] == winner_list[0]:
        print("Tie game")
    
    return winner_list   

#the function to run the game
def run_game():
    mancala_list = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
    
    player_1 = get_player('1')
    player_2 = get_player('2')

    #top cups 2d list
    top_cups = [['Cup   ', '     1', 'Stones', '     4', '      '],
                ['Cup   ', '     2', 'Stones', '     4', '      '],
                ['Cup   ', '     3', 'Stones', '     4', '      '],
                ['Cup   ', '     4', 'Stones', '     4', '      '],
                ['Cup   ', '     5', 'Stones', '     4', '      '],
                ['Cup   ', '     6', 'Stones', '     4', '      ']]
    
    #bottom cups 2d list
    bottom_cups = [['Cup   ', '    13', 'Stones', '     4', '      '],
                ['Cup   ', '    12', 'Stones', '     4', '      '],
                ['Cup   ', '    11', 'Stones', '     4', '      '],
                ['Cup   ', '    10', 'Stones', '     4', '      '],
                ['Cup   ', '     9', 'Stones', '     4', '      '],
                ['Cup   ', '     8', 'Stones', '     4', '      ']]
    
    #Second player, mancala_a, cup position 0
    mancala_a = ['      ', '      ', '      ', 'Boris ', '      ', '      ', '      ', 'Stones', '     0', '      ', '      ']

    #First player, mancala_b, cup position 7
    mancala_b = ['      ', '      ', '      ', 'Abby  ', '      ', '      ', '      ', 'Stones', '     0', '      ', '      ']
    
    #to replace the mancala_a and mancala_b lists with player names
    mancala_b[3] = player_1
    mancala_a[3] = player_2
    
    draw_board(top_cups, bottom_cups, mancala_a, mancala_b)
    
    #checking to see if the game isn't over yet
    while not is_game_over(mancala_list):
        take_turn(player_1, mancala_list, top_cups, bottom_cups, mancala_a, mancala_b)
        
        if not is_game_over(mancala_list):
            take_turn(player_2, mancala_list, top_cups, bottom_cups, mancala_a, mancala_b)
    
    #checking to see if the game has ended        
    if is_game_over(mancala_list):
        win_game(mancala_list, player_1, player_2)


if __name__ == "__main__":
    run_game()


