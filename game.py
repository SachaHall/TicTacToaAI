from board import Board
class Game:
    def __init__(self):
        self.board = Board(3)
    def aiPlays(self):
        self.board.playBestMove()
        self.board.printBoard()
    def userPlays(self):
        row = col = 0
        while (not self.board.is_valid(row-1,col-1)):
            row = int(input("row: "))
            col = int(input("column: "))
        self.board.move(row-1,col-1)
        self.board.printBoard()
    def console_begin(self):
        a = ""
        while (a!='y' and a!='n'):
            a = input("Do you want to play first? y/n")
        self.aiFirst = True if a=='n' else False
        if self.aiFirst:
            print("ai plays... \n")
            self.aiPlays()
        while (self.board.evaluateBoard()==0):
            if (self.board.xTurn==self.aiFirst):
                print("ai plays... \n")
                self.aiPlays()
            else:
                self.userPlays()
        print("done")
    def guiBegin():
        pass