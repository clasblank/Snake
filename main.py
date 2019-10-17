from snakePresenter import SnakePresenter
from snakeModel import SnakeModel
from snakeGUI import SnakeGUI


def main():
    sm = SnakeModel(15)
    gui = SnakeGUI()
    sc = SnakePresenter(sm, gui)
    sc.run()

if __name__ == "__main__":
    main()