class TicTacToe_board:
    def __init__(self):
        self.board = None
        self.mark = None
        self.player_mark = None
        
        
    def display_board(self):
        print('     |     |')
        print('  ' + self.board[0] + '  |  ' + self.board[1] + '  |  ' + self.board[2])
        print('     |     |')
        print('-----------------')
        print('     |     |')
        print('  ' + self.board[3] + '  |  ' + self.board[4] + '  |  ' + self.board[5])
        print('     |     |')
        print('-----------------')
        print('     |     |')
        print('  ' + self.board[6] + '  |  ' + self.board[7] + '  |  ' + self.board[8])
        print('     |     |')
        print('                 ')

    
    
    def board_copy(self, board):
        return [x for x in board]
    
    # Check if a person has won
    def check_win(self, player, board):# Player is X or O
        ## If the player has won then there must be "n" consecutive Player values
        #Check Horizontal
        board = [board[i:i+3] for i in range(0, len(board), 3)]
        horizontal = [player]*3 in board

        #Check Vertical
        vertical = [player]*3 in [list(x) for x in list(zip(*board))]

        #Check Right Diagnol
        left = all(board[i][i] == player for i in range(3))

        #Left Diagnol
        right = all(board[i][2-i] == player for i in range(3))

        return horizontal or vertical or left or right
    
    def check_draw(self):
        return " " not in self.board
    
    def test_win_move(self, move, player_mark, board):
        test_b = self.board_copy(board)
        test_b[move] = player_mark
        return self.check_win(player_mark, test_b)
    
    
    def test_fork_move(self, move, player_mark, board):
        # Determines if a move opens up a fork
        test_b = self.board_copy(board)
        test_b[move] = player_mark
        winning_moves = 0
        for i in range(9):
            if test_b[i] and self.test_win_move(i, player_mark, test_b):
                winning_moves += 1
        return winning_moves >= 2
    
    def final_stategy(self):
        # Play center
        if self.board[4] == ' ':
            return 4
        # Play a corner
        for i in [0, 2, 6, 8]:
            if self.board[i] == ' ':
                return i
        #Play a side
        for i in [1 ,3, 5, 7]:
            if self.board[i] == ' ':
                return i
        
        
    def get_agent_move(self):
        # Check if Agent wins or Sabatoge if Players wins
        for i in range(9):
            if self.board[i] == ' ':
                if self.test_win_move(i, self.mark, self.board):
                    return i
                elif self.test_win_move(i, self.player_mark, self.board):
                    return i
        temp = None
        count = 0
        for i in range(9):
            if self.board[i] == ' ':
                if self.test_fork_move(i, self.mark, self.board):
                    return i
                elif self.test_fork_move(i, self.player_mark, self.board):
                    temp = i
                    count += 1
        if count == 1:
            return temp
        elif count == 2:
            for i in [1, 3, 5, 7]:
                if self.board[i] == ' ':
                    return i
        return self.final_stategy()
        
    # Player plays    
    def player_moves(self):
        self.display_board()
        print("Which spot (0-8)")
        move = int(input()) 
        while self.board[move] != " ":
            self.display_board()
            print("Please pick a valid move (0-8)")
            move = int(input())
        self.board[move] = self.player_mark
        self.display_board()

    #Agent plays
    def agent_moves(self):
        move = self.get_agent_move()
        self.board[move] = self.mark
        self.display_board()
    
    # Assemble the game
    def tictactoe(self):
        Playing = True
        while Playing:
            self.board = [" " for i in range(9)]
            # Choose Marks
            print('X or O')
            self.player_mark = input()
            self.mark = 'X' if self.player_mark == "O" else "O"

            #Choose start
            print("Want to go first [y,n]")
            flag = '1' if input() == 'y' else '0'

            Ingame = True
            while Ingame:

                if flag == '1':
                    self.player_moves()
                    mark = self.player_mark
                else:
                    self.agent_moves()
                    mark = self.mark
                
                #Check if someone won
                if self.check_win(mark, self.board):
                    Ingame = False
                    if mark == self.player_mark:
                        print("Player wins!!!")
                    else:
                        print("Agent wins")
                    break
                
                # Check if game Draws
                if self.check_draw():
                    print('Draw!!!')
                    break
                
                #Switch to comp or person moves
                flag = '0' if flag == '1' else '1'
            
            # Another game 
            print("Another game [y,n]?")
            if input() == 'n':
                Playing = False
        print('Thank you for playing!')

b = TicTacToe_board()
b.tictactoe()

 
     
