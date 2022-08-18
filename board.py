import math
import random
class Board:
    def __init__(self,size):
        self.size = size
        self.board = [[None for i in range(3)] for j in range(3)]
        self.xTurn = True
    def evaluateBoard(self):
        board = self.board #improve readabilty
        for row in board:
            if None in row:
                continue
            if row[0]==row[1] and row[1]==row[2]:
                if row[0]:
                    return 10
                return -10
        for i in range(1,3):
            if None in [board[j][i] for j in range(3)]:
                continue
            if (board[0][i]==board[1][i] and board[1][i]==board[2][i]):
                if board[0][i]:
                    return 10
                return -10
        if board[0][0]==board[1][1] and board[1][1]==board[2][2]:
            if board[1][1]:
                return 10
            return -10
        return 0

    def move(self,row,col):
        self.board[row][col] = self.xTurn
        self.xTurn = not self.xTurn

    def playBestMove(self):
        best = ()
        bestScore = -math.inf
        for row in range(3):
            for col in range(3):
                if self.board[row][col] is not None:
                    self.board[row][col] = self.xTurn
                    score = self.miniMax(0,False)
                    self.board[row][col] = None
                    if score>bestScore:
                        bestScore = score
                        best = (row, col)
        self.move(best[0],best[1])

    def miniMax(self):
        return 1-2*random.randint(0,1) #todo: implement minimax