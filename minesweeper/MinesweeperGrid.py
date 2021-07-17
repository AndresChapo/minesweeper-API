import random

VACIO = 0
MINE = 'x'

class MinesweeperGrid:
    def __init__(self, sizes, mines_cuantities):
        self.sizes = sizes
        self.mines_cuantities = mines_cuantities
        self.grid = self.new_grid()
        #        self.set_values_in_grid()
        self.swept = set()

    def new_grid(self):
        grid = []
        for y in range(self.sizes):
            grid.append([])
            for x in range(self.sizes): grid[y].append(VACIO)

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
                if (y,x) in self.swept:
                    field[y].append(str(self.grid[y][x]))
                else:
                    field[y].append('.')

        for i in range(len(field)):
            field_string += str(field[i]) + '  \n'

        return field_string


grid = MinesweeperGrid(10, 10)
grid.grid[1][1] = 1
grid.grid[1][2] = 2
grid.grid[1][3] = 3
print(grid.grid)

print(grid)