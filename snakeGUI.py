import tkinter as tk
from snakeModel import SnakeModel

class SnakeGUI:
    def __init__(self):
        self.presenter = None
        self.squareSize = 20
        self.startDifficulty = 5
        self.canvasHeight = 30
        self.root = tk.Tk()
        self.root.wm_title("The Awesome Snake Game")
        self.rects = []


        self.numToColor = {
            0: "black",
            1: "red",
            2: "yellow"
        }

    def run(self):
        self.root.mainloop()
    
    def createBoard(self, size):
        self.window = tk.Frame(self.root, width=size*self.squareSize, height=size*self.squareSize)
        self.window.winfo_toplevel().title = "The Awesome Snake Game"
        self.window.pack()
        self.boardCanvas = tk.Canvas(self.window, width=size*self.squareSize, height=size*self.squareSize)
        self.createRectangles(size)

        self.menuCanvas = tk.Canvas(self.window, width=size*self.squareSize, height=self.canvasHeight)
        self.scoreCanvas = tk.Canvas(self.window, width=size*self.squareSize, height=self.canvasHeight)
        self.sliderCanvas = tk.Canvas(self.window, width=size*self.squareSize, height=self.canvasHeight)
        self.score = self.scoreCanvas.create_text(size*self.squareSize/2, self.canvasHeight/2, fill = "green", text = f"Score: 0")
        self.quitButton = tk.Button(self.menuCanvas, text = "Quit", command = self.presenter.exitAll)
        self.restartButton = tk.Button(self.menuCanvas, text = "Restart", command = self.presenter.restart)
        self.slider = tk.Scale(self.sliderCanvas, from_=1, to=9, orient="horizontal", command = self.presenter.setDifficulty)
        self.slider.set(self.startDifficulty)

        self.quitButton.pack()
        self.restartButton.pack()
        self.boardCanvas.pack()
        self.scoreCanvas.pack()
        self.slider.pack()
        self.menuCanvas.pack()
        self.sliderCanvas.pack()

    def createRectangles(self, size):
        for i in range(size):
            for j in range(size):
                self.rects.append(
                    self.boardCanvas.create_rectangle(j * self.squareSize,
                    i * self.squareSize, (j + 1)*self.squareSize,
                    (i + 1)*self.squareSize, fill = self.numToColor[0]))

    def updateBoard(self, board):
        for i, val in enumerate(board):
            self.boardCanvas.itemconfig(self.rects[i], fill = self.numToColor[val])

    def updateScore(self, score):
        self.scoreCanvas.itemconfig(self.score, text = f"Score: {score}")

    def exit(self):
        self.window.quit()
        self.root.quit()

if __name__ == "__main__":
    SnakeGUI()