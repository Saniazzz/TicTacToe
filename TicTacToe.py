class TicTacToe:
    def print_board(self, board):
        for i in range(3):
            print "",
            for j in range(3):
                if board[i * 3 + j] == 1:      # 1 represents X
                    print 'X',
                elif board[i * 3 + j] == 0:
                    print 'O',                 # 0 represents 0
                elif board[i * 3 + j] != -1:   # -1 represents ' '
                    print board[i * 3 + j] - 1,
                else:
                    print ' ',
                if j != 2:
                    print "|",
            print
            if i != 2:
                print "-----------"
            else:
                print

    def print_instr(self):
        print "Each number represents one of 9 cells from the board:"
        self.print_board([2, 3, 4, 5, 6, 7, 8, 9, 10])

    def get_valid_turn(self, turn):
        valid = False
        while not valid:
            try:
                user = raw_input("Where to place " + turn + " (1-9)? ")
                user = int(user)
                if user >= 1 and user <= 9:
                    return user - 1
                else:
                    print "Invalid move! Please try again.\n"
                    self.print_instr()
            except Exception:
                print user + " is not a valid move! Please try again.\n"

    def check_if_won(self, board):
        winCond = ((1, 2, 3), (4, 5, 6), (7, 8, 9),  # every combination
                   (1, 4, 7), (2, 5, 8), (3, 6, 9),  # at which
                   (1, 5, 9), (3, 5, 7))             # player wins
        for each in winCond:
            try:
                if board[each[0] - 1] == board[each[1] - 1] and \
                   board[each[1] - 1] == board[each[2] - 1]:
                    return board[each[0] - 1]
            except:
                pass
        return -1

    def quit_game(self, board, message):
        self.print_board(board)
        print message
        quit()

    def run(self):
        # printing instructions
        self.print_instr()
        # setting board to default settings when all cells are ' '
        board = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
        gameOver = False
        move = 0

        print "Game start"
        while not gameOver:
            # printing board
            self.print_board(board)
            print str(move + 1) + " turn:"
            # checking whose move current turn is
            if move % 2 == 0:
                turn = 'X'
            else:
                turn = 'O'
            # geting user input
            user = self.get_valid_turn(turn)
            while board[user] != -1:
                print "Invalid move! Cell already taken. Please try again.\n"
                user = self.get_valid_turn(turn)
            board[user] = 1 if turn == 'X' else 0
            # advancing move and checking for end game
            move += 1
            if move > 4:  # end game is only possible at 4+ moves
                winner = self.check_if_won(board)
                if winner != -1:
                    out = "The winner is "
                    out += "X" if winner == 1 else "O"
                    self.quit_game(board, out)
                elif move == 9:
                    self.quit_game(board, "No winner")
