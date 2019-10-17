import tkinter as tk
import random
from enum import Enum

class Direction(Enum):
    RIGHT = 0
    DOWN  = 1
    LEFT  = 2
    UP    = 3

    @classmethod
    def getIncrement(cls, direction, size):
        CONSTANTS = {
            cls.RIGHT: 1,
            cls.DOWN: 1,
            cls.LEFT: -1,
            cls.UP: -1,
        }
        if direction == cls.LEFT or direction == cls.RIGHT:
            size = 1
        return CONSTANTS[direction] * size
    
    @classmethod
    def isOrthogonal(cls, direction1, direction2):
        if direction1 == cls.RIGHT or direction1 == cls.LEFT:
            return direction2 == cls.UP or direction2 == cls.DOWN
        return direction2 == cls.RIGHT or direction2 == cls.LEFT


class SnakeModel:
    EMPTY_SPACE = 0
    SNAKE = 1
    FOOD = 2

    def __init__(self, size = 24, snakeStart = 0):
        self.size = size
        self.snakeStart = snakeStart
        self.initBoard()

    def initBoard(self):
        self.currentDirection = Direction.RIGHT
        self.addNextRound = False
        self.canChangeDirection = True
        self.score = 0
        self.board = [0] * self.size ** 2

        # Initialize snake at top left corner
        self.snake = [self.snakeStart]
        self.board[0] = SnakeModel.SNAKE 
        self.putFood()
        self.currentlyEating = []

    def putFood(self):
        self.board[random.sample(
            set(range(self.size ** 2)) - set(self.snake), 1)[0]
            ] = SnakeModel.FOOD

    def moveSnake(self):
        self.canChangeDirection = True
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i] = self.snake[i - 1]

        self.snake[0] += Direction.getIncrement(self.currentDirection, self.size)

    def gameOver(self):
        return self.snake[0] + Direction.getIncrement(self.currentDirection, self.size) in self.snake or self.hitsEdge()
    
    def hitsEdge(self):
        return self.currentDirection == Direction.RIGHT and self.snake[0] in range(self.size - 1, self.size ** 2 - 1, self.size) \
               or self.currentDirection == Direction.DOWN and self.snake[0] in range(self.size ** 2 - self.size, self.size ** 2) \
               or self.currentDirection == Direction.LEFT and self.snake[0] in range(0, self.size ** 2 - self.size + 1, self.size) \
               or self.currentDirection == Direction.UP and self.snake[0] in range(self.size)

    def snakeAteFood(self):
        return self.board[self.snake[0]] == SnakeModel.FOOD

    def addFoodToSnake(self):
        self.currentlyEating.append(self.snake[0])
        self.putFood()
        self.score += 1

    def addTail(self):
        if self.addNextRound:
            self.snake.append(self.currentlyEating.pop(0))
            self.addNextRound = False
        if self.currentlyEating and self.snake[-1] == self.currentlyEating[0]:
            self.addNextRound = True
    
    def changeDirection(self, direciton):
        if self.canChangeDirection and \
         Direction.isOrthogonal(self.currentDirection, direciton):
            self.currentDirection = direciton
            self.canChangeDirection = False

    def updateBoard(self):
        self.board = [0 if block != SnakeModel.FOOD else block for block in self.board]
        for snakePartIndex in self.snake:
            self.board[snakePartIndex] = SnakeModel.SNAKE

    def printBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.board[i * self.size + j], end=" ")
            print()
        
        print()


if __name__ == "__main__":
    
    sm = SnakeModel()
