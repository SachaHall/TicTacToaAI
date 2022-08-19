class Board:
    def boolToChar(val):
        match val:
            case True:
                return 'x'
            case False:
                return 'o'
            case None:
                return ' '
    def __init__(self,size):
        self.size = size
        self.board = [[None for i in range(3)] for j in range(3)]
        self.xTurn = True

    def is_valid(self, row, col):
        return row>=0 and row<3 and col>=0 and col<3 and self.board[row][col] is None

    def game_over(self):
        a = True
        for row in self.board:
            if None in row:
                a = False
        return a

    def evaluateBoard(self):
        board = self.board #improve readabilty
        for row in board:
            if None in row:
                continue
            if row[0]==row[1] and row[1]==row[2]:
                if row[0]:
                    return 10
                return -10
        for i in range(3):
            if None in [board[j][i] for j in range(3)]:
                continue
            if (board[0][i]==board[1][i] and board[1][i]==board[2][i]):
                if board[0][i]:
                    return 10
                return -10
        if board[1][1] is None:
            return 0
        if (board[0][0]==board[1][1] and board[1][1]==board[2][2]) or (board[0][2]==board[1][1] and board[1][1]==board[2][0]):
            if board[1][1]:
                return 10
            return -10
        return 0

    def move(self,row,col):
        self.board[row][col] = self.xTurn
        self.xTurn = not self.xTurn

    def playBestMove(self):
        best = (-1,-1)
        bestScore = -1000 if self.xTurn else 1000
        for row in range(3):
            for col in range(3):
                if self.board[row][col] is None:
                    self.board[row][col] = self.xTurn
                    score = self.miniMax(0,not self.xTurn)
                    self.board[row][col] = None
                    if self.xTurn:
                        if score>bestScore:
                            bestScore = score
                            best = (row, col)
                    if not self.xTurn:
                        if score<bestScore:
                            bestScore = score
                            best = (row, col)
        self.move(best[0],best[1])
        #print(bestScore)

    def miniMax(self, depth, maxiTurn):
        state = self.evaluateBoard()
        if state!=0:
            if state>0:
                return state-depth
            return state+depth
        elif self.game_over():
            return 0

        if maxiTurn:
            best = -1000
            for row in range(3):
                for col in range(3):
                    if self.board[row][col] is None:
                        self.board[row][col] = True
                        best = max(best,self.miniMax(depth+1,False))
                        self.board[row][col] = None
            return best

        best = 1000
        for row in range(3):
            for col in range(3):
                if self.board[row][col] is None:
                    self.board[row][col] = False
                    best = min(best,self.miniMax(depth+1,True))
                    self.board[row][col] = None
        return best


    def printBoard(self):
        for row in self.board:
            print('|'.join([Board.boolToChar(i) for i in row]))
            print(2*len(row)*'_')