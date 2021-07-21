from minesweeper.MinesweeperGrid import MinesweeperGrid
from data_access_object import *


# OK - add game_status
# OK - add translators to MinesweeperGrid to db_Grid and vice versa
# OK new_game(sizes,mines) - save and return the grid
# play_on_this_grid(id_game,row,column, flag) - save and return the grid

class Game:

    def __init__(self):
        pass

    def play_on_this_grid(self, id_game, row, column, flag):
        # 1. fetch game
        self.grid = Grid_to_Minesweeper(get_one_grid(id_game))
        # 2. validate_coordinates
        if self.validate_coordinates(row, column) is False: return -1
        # 3. check that is not a flag
        # 4. sweep
        self.grid.sweep(row, column)
        # 5. Chek if the game ended
        if self.grid.game_status != 1:
            for y in range(self.grid.sizes):
                for x in range(self.grid.sizes):
                    self.grid.swept.add((y, x))  # clean the board
        # 5. persist (update)
        update_grid(id_game, self.grid)
        # 6. return something
        return self.grid.game_status

    def new_game_persist(self, sizes=10, mines=1):
        self.grid = MinesweeperGrid(sizes, mines)
        return persist_new_grids(self.grid)  # Returns a db_grid

    def new_game(self, sizes=10, mines=1):
        self.grid = MinesweeperGrid(sizes, mines)

    def validate_coordinates(self, row, column):
        if row < 0 or row >= self.grid.sizes or column < 0 or column >= self.grid.sizes:
            return False
        else:
            return True

    def run_on_console(self):
        while self.grid.game_status == 1:
            # For debug
            print("Holes done(swept): ", len(self.grid.swept))
            print(str(self.grid.grid))
            print('#' * 50)
            print(list(str(l) for l in range(0, self.grid.sizes)))
            # Real game
            print(self.grid)
            row = int(input("Row: "))
            column = int(input("Column: "))
            if self.validate_coordinates(row, column):
                self.grid.sweep(row, column)
            else:
                print("Invalid coordinates!")
                continue

        for y in range(self.grid.sizes):
            for x in range(self.grid.sizes):
                self.grid.swept.add((y, x))  # clean the board
        print(self.grid)
        if self.grid.game_status == 2:
            print("You Win!")
        elif self.grid.game_status == 0:
            print("Game Over!")

    def run_on_console_persiting(self, sizes, mines):
        db_grid = self.new_game_persist(sizes, mines)
        while self.grid.game_status == 1:
            # For debug

            # Real game
            print(self.grid)
            row = int(input("Row: "))
            column = int(input("Column: "))
            if self.play_on_this_grid(db_grid.id_game,row,column,0) == -1:
                print("Invalid coordinates!")
                continue

        print(self.grid)
        if self.grid.game_status == 2:
            print("You Win!")
        elif self.grid.game_status == 0:
            print("Game Over!")
