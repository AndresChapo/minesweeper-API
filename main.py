from data_access_object import *
from minesweeper.Game import Game
from minesweeper.MinesweeperGrid import MinesweeperGrid
from models import Grids

if __name__ == '__main__':
    game = Game()
# Play the game persisting
    game.run_on_console_persiting(20, 10)

# Get and play this id_game
#    game.play_on_this_grid(15, 0, 3, 1)

#    game.new_game(5, 23)
#    game.grid.sweep(1,1)
#    game.grid.sweep(2,2)

# NEW game and persist
#    db_grid = game.new_game_persist(5, 1)
#    print("db Grid: ", db_grid.grid)
#    game_grid = MinesweeperGrid(5, 23)
#    game.run_on_console()
#    db_grid = Grids(1, 1, 1, [1,2,3], '(2,2)', 1)
#    db_grid.to_Grid(game_grid, 1)
#    game_grid.to_Minesweeper(db_grid)
#    db_grid = MinesweeperGrid_to_Grid(game_grid, 1)
#    game_grid = Grid_to_Minesweeper(db_grid)
#    print("game Grid: ", game.grid.grid)
#    print("game Grid[0]: ", game.grid.grid[0])
#    print("game set swept: ", game.grid.swept)
