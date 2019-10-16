from pynput import keyboard
from snakeModel import Direction
import concurrent.futures
import time

class SnakePresenter:
    def __init__(self, snakeModel, snakeGUI):
        self.snakeModel = snakeModel
        self.snakeGUI = snakeGUI

        self.playerExited = False

        self.keyToDirection = {
            keyboard.Key.down: Direction.DOWN,
            keyboard.Key.up: Direction.UP,
            keyboard.Key.left: Direction.LEFT,
            keyboard.Key.right: Direction.RIGHT,
        }

        self.snakeGUI.createBoard(self.snakeModel.size)
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.submit(self.setUpListener)
            executor.submit(self.stepSnake)
            executor.submit(self.snakeGUI.run())
        print("Exiting all")

    def stepSnake(self):
        while True:
            self.snakeModel.moveSnake()
            
            if self.snakeModel.snakeAteFood():
                self.snakeModel.addFoodToSnake()
                self.snakeGUI.updateScore(self.snakeModel.score)

            self.snakeModel.addTail()
            self.snakeModel.updateBoard()

            self.snakeGUI.updateBoard(self.snakeModel.board)
            time.sleep(.2)
            if self.snakeModel.gameOver() or self.playerExited:
                self.exitAll()
                return False

    def setUpListener(self):
        with keyboard.Listener( 
            on_press=self.onPress,
            #on_release=on_release
            ) as listener:
            listener.join()
        print("listener finished")
            
    def onPress(self, key):
        if key == keyboard.Key.esc:
            self.playerExited = True
        # Stop listener
            return False

        elif key in [keyboard.Key.down, keyboard.Key.up, keyboard.Key.left, keyboard.Key.right]:
            self.snakeModel.changeDirection(self.keyToDirection[key])

        return True

    def exitAll(self):
        keyboard.Controller().press(keyboard.Key.esc)
        self.snakeGUI.exit()

if __name__ == "__main__":
    from snakeModel import SnakeModel
    SnakePresenter(SnakeModel(24))