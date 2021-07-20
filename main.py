from minesweeper.Game import Game
from minesweeper.MinesweeperGrid import MinesweeperGrid

if __name__ == '__main__':
    game = Game()
    game.new_game(10, 10)
    game.run_on_console()
