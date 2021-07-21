from minesweeper.MinesweeperGrid import MinesweeperGrid

# add game_status
# add translators to MinesweeperGrid to db_Grid and vice versa
# new_game(sizes,mines) - save and return the grid
# play_this_grid(id_game,row,column, flag) - save and return the grid

class Game:

    def __init__(self):
        pass

    def new_game(self, sizes=10, mines=1):
        self.grid = MinesweeperGrid(sizes, mines)

    def validate_coordinates(self, row, column):
        if row < 0 or row >= self.grid.sizes or column < 0 or column >= self.grid.sizes:
            return False
        else:
            return True

    def run_on_console(self):
#        continue_game = True
        # max_cuantities_of_sweeps = (self.grid.sizes * self.grid.sizes) - self.grid.mines_cuantities
        # while len(self.grid.swept) < max_cuantities_of_sweeps:
        while self.grid.game_status == 1:
            # For debug
            print("Holes done(swept): ", len(self.grid.swept))
            print(str(self.grid.grid))
            print('#'*50)
            print(list(str(l) for l in range(0,self.grid.sizes)))
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
                self.grid.swept.add((y, x)) # clean the board
        print(self.grid)
        if self.grid.game_status == 2:
            print("You Win!")
        elif self.grid.game_status == 0:
            print("Game Over!")