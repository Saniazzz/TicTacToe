class TicTacToe:
    def printBoard(self, board):
        for i in range(3):
            print "",
            for j in range(3):
                if board[i*3+j] == 1:      #1 represents X
                    print 'X',
                elif board[i*3+j] == 0:
                    print 'O',	           #0 represents 0
                elif board[i*3+j] != -1:   #-1 represents ' '
                    print board[i*3+j]-1,
                else:
                    print ' ',
                if j != 2:
                    print "|",
            print
            if i != 2:
                print "-----------"
            else: 
                print 

    def printInstr(self):
        print "Each number represents one of 9 cells from the board:"
        self.printBoard([2,3,4,5,6,7,8,9,10])

    def getValidTurn(self, turn):
        valid = False
        while not valid:
            try:
                user = raw_input("Where to place " + turn + " (1-9)? ")
                user = int(user)
                if user >= 1 and user <= 9:
                    return user-1
                else:
                    print "Invalid move! Please try again.\n"
                    self.printInstr()
            except Exception:
                print user + " is not a valid move! Please try again.\n"

    def run(self):
        #printing instructions
        self.printInstr()
