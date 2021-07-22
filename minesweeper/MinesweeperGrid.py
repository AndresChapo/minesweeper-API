import random
from models import Grids

EMPTY = 0
MINE = 9 # 'x' -1
FLAG = '?'

class MinesweeperGrid:

    def __init__(self, sizes, mines_cuantities):
        self.sizes = sizes
        self.mines_cuantities = mines_cuantities
        self.grid = self.new_grid()
        self.add_points_to_grid()
        self.swept = set()
        self.flags = set()
        self.game_status = 1 # 0 = Game Over; 1 = Game continues; 2 = Win

    def new_grid(self):
        grid = []
        for y in range(self.sizes):
            grid.append([])
            for x in range(self.sizes): grid[y].append(EMPTY)

        mines_underground = 0
        while mines_underground < self.mines_cuantities:
            pos_row = random.randrange(0, self.sizes, 1)
            pos_col = random.randrange(0, self.sizes, 1)
            #            print(pos_row,pos_col)
            if grid[pos_row][pos_col] == MINE:
                continue
            else:
                grid[pos_row][pos_col] = MINE
                mines_underground += 1
        return grid

    def __str__(self):
        field = []
        field_string = ''

        for y in range(self.sizes):
            field.append([])
            for x in range(self.sizes):
                if (y, x) in self.swept:
                    field[y].append(str(self.grid[y][x]))
                else:
                    if (y, x) in self.flags:
                        field[y].append(FLAG)
                    else:
                        field[y].append('.')

        for i in range(len(field)):
            field_string += str(field[i]) + '  \n' # Turn the list into a string

        return field_string

    def plant_flag(self, row, column):
        if ((row, column)) in self.flags:
            self.flags.remove((row, column))
        else:
            self.flags.add((row, column))

    def sweep(self, row, column): # return True if it's ok, False if it's a mine
        self.swept.add((row, column))
        if self.grid[row][column] == MINE:
            self.game_status = 0
            return False
        elif self.grid[row][column] > 0: # it could be replaced be EMPTY
            self.check_if_player_won()
            return True

        from_row = max(0, row - 1)
        until_row = min(self.sizes - 1, row + 1) + 1
        for y in range(from_row, until_row):
            from_column = max(0, column - 1)
            until_column = min(self.sizes - 1, column + 1) + 1
            for x in range(from_column, until_column):
                if (y, x) in self.swept: continue
                self.sweep(y, x)
        self.check_if_player_won()
        return True

    def check_if_player_won(self):
        max_cuantities_of_sweeps = (self.sizes * self.sizes) - self.mines_cuantities
        # print("max_cuantities_of_sweeps: ", max_cuantities_of_sweeps)
        if len(self.swept) < max_cuantities_of_sweeps:
            self.game_status = 1
        else:
            self.game_status = 2

    def add_points_to_grid(self):
        rang = range(self.sizes)
        for y in rang:
            for x in rang:
                if self.grid[y][x] == MINE: continue
                else: self.grid[y][x] = self.get_near_mines(y,x)

    def get_near_mines(self, row, column):
        num_near_mines = 0
        from_row = max(0, row - 1)
        until_row = min(self.sizes - 1, row + 1) + 1
        for y in range(from_row, until_row):
            from_column = max(0, column - 1)
            until_column = min(self.sizes - 1, column + 1) + 1
            for x in range(from_column, until_column):
                if y == row and x == column: continue
                if self.grid[y][x] == MINE: num_near_mines += 1

        return num_near_mines
