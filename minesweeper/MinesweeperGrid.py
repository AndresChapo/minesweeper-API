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

    def sweep(self, row, column):
        self.swept.add((row, column))
        if self.grid[row][column] == MINE:
            return False
        elif self.grid[row][column] > 0:
            return True

        desde = max(0, row - 1)
        hasta = min(self.sizes - 1, row + 1) + 1
        for r in range(desde, hasta):
            desde_columna = max(0, column - 1)
            hasta_columna = min(self.sizes - 1, column + 1) + 1
            for c in range(desde_columna, hasta_columna):
                if (r, c) in self.swept:
                    continue
                self.sweep(r, c)

        return True

grid = MinesweeperGrid(10, 10)
grid.grid[1][1] = 1
grid.grid[1][2] = 2
grid.grid[1][3] = 3
print(grid.grid)
grid.sweep(1,1)
grid.sweep(1,2)
grid.sweep(1,3)
grid.sweep(1,4)

print(grid)