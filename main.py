from data_access_object import *
from minesweeper.Game import Game
from minesweeper.MinesweeperGrid import MinesweeperGrid
from models import Grids

if __name__ == '__main__':
    game = Game()
    db_grid = game.new_game_persist(5, 23)
#    game_grid = MinesweeperGrid(5, 23)
#    game.run_on_console()
#    db_grid = Grids(1, 1, 1, [1,2,3], '(2,2)', 1)
#    db_grid.to_Grid(game_grid, 1)
#    game_grid.to_Minesweeper(db_grid)
    #db_grid = MinesweeperGrid_to_Grid(game_grid, 1)
#    game_grid = Grid_to_Minesweeper(db_grid)
#    print("game Grid: ", game_grid.grid)
    print("db Grid: ", db_grid.grid)
#    print(type(game.grid))
#    print(type(db_grid))