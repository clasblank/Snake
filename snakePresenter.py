from pynput import keyboard
from snakeModel import Direction
import concurrent.futures
import time

class SnakePresenter:
    def __init__(self, snakeModel, snakeGUI):
        self.snakeModel = snakeModel
        self.snakeGUI = snakeGUI
        self.snakeGUI.presenter = self
        self.difficulty = 0.25
        self.playerExited = False
        self.freeze = False

        self.keyToDirection = {
            keyboard.Key.down: Direction.DOWN,
            keyboard.Key.up: Direction.UP,
            keyboard.Key.left: Direction.LEFT,
            keyboard.Key.right: Direction.RIGHT,
        }

        self.snakeGUI.createBoard(self.snakeModel.size)

    def run(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(self.setUpListener)
            executor.submit(self.startGame)
            executor.submit(self.snakeGUI.run())
    
    def restart(self):
        self.snakeGUI.updateScore(0)
        self.freeze = False
        self.snakeModel.initBoard()

    def setDifficulty(self, val):
        self.difficulty = (abs(int(val) - 9) + 1.02) / 25

    def startGame(self):
        while True:

            if self.playerExited:
                return False

            elif not self.freeze:
                self.stepSnake()
            
            if self.snakeModel.gameOver():
                self.freeze = True
    
    def stepSnake(self):
        self.snakeModel.moveSnake()
                
        if self.snakeModel.snakeAteFood():
            self.snakeModel.addFoodToSnake()
            self.snakeGUI.updateScore(self.snakeModel.score)

        self.snakeModel.addTail()
        self.snakeModel.updateBoard()

        self.snakeGUI.updateBoard(self.snakeModel.board)
        time.sleep(self.difficulty)
    

    def setUpListener(self):
        with keyboard.Listener( 
            on_press=self.onPress,
            ) as listener:
            listener.join()
            
    def onPress(self, key):
        if key == keyboard.Key.esc:
            self.exitAll()
            return False

        elif key in [keyboard.Key.down, keyboard.Key.up, keyboard.Key.left, keyboard.Key.right] and not self.freeze:
            self.snakeModel.changeDirection(self.keyToDirection[key])

        return True

    def exitAll(self):
        self.playerExited = True
        keyboard.Controller().press(keyboard.Key.esc)
        self.snakeGUI.exit()

if __name__ == "__main__":
    from snakeModel import SnakeModel
    from snakeGUI import SnakeGUI
    SnakePresenter(SnakeModel(24), SnakeGUI())