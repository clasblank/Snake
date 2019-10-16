import tkinter as tk
from snakeModel import SnakeModel

class SnakeGUI:
    def __init__(self):

        self.squareSize = 20
        self.root = tk.Tk()
        self.root.title = "The Awesome Snake Game"
        #root.geometry("500x500")
        self.rects = []


        self.numToColor = {
            0: "black",
            1: "red",
            2: "yellow"
        }

    def run(self):
        self.root.mainloop()
        print("GUI exited")
    
    def createBoard(self, size):
        self.window = tk.Frame(self.root, width=size*self.squareSize, height=size*self.squareSize)
        self.window.pack()
        self.boardCanvas = tk.Canvas(self.window, width=size*self.squareSize, height=size*self.squareSize)

        for i in range(size):
            for j in range(size):
                rect = self.boardCanvas.create_rectangle(j * self.squareSize, i * self.squareSize, (j + 1)*self.squareSize, (i + 1)*self.squareSize, fill=self.numToColor[0])
                self.rects.append(rect)

        self.scoreCanvas = tk.Canvas(self.window, width=size*self.squareSize, height=30)
        self.score = self.scoreCanvas.create_text(size*self.squareSize/2, 15, fill = "green",text=f"Score: 0")
        # self.score = self.scoreCanvas.create_text(size*self.squareSize/2, size*self.squareSize, text="0")
        self.boardCanvas.pack()
        self.scoreCanvas.pack()

    def updateBoard(self, board):
        for i, val in enumerate(board):
            self.boardCanvas.itemconfig(self.rects[i], fill=self.numToColor[val])

    def updateScore(self, score):
        self.scoreCanvas.itemconfig(self.score, text=f"Score: {score}")

    def exit(self):
        self.window.quit()
        self.root.quit()

if __name__ == "__main__":
    SnakeGUI()