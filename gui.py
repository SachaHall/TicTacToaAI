import tkinter as tk
from board import Board
class Gui:
    def __init__(self):
        self.board = Board(3)
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=600, height=600)
        self.canvas.pack()
        for i in range(1,3):
            self.canvas.create_line(0, 200*i, 600, 200*i, width=1)
            self.canvas.create_line(200*i,0,200*i,600, width=1)
        self.root.title("Tic Tac Toe")
        self.canvas.bind("<Button-1>", self.callback)
        self.root.mainloop()
    def callback(self, event):
        row, col = event.x//200, event.y//200
        if (not self.board.is_valid(row,col)):
            return
        self.board.move(row,col)
        self.canvas.create_text(row*200+100, col*200+100, text="X", fill="white", font = ('helvetica','60'))
        best = self.board.playBestMove()
        self.canvas.create_text(best[0]*200+100, best[1]*200+100, text="O", fill="white", font = ('helvetica','60'))