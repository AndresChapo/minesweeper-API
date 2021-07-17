import random


class MinesweeperGrid:
    def __init__(self, sizes, mines_cuantities):
        self.sizes = sizes
        self.mines_cuantities = mines_cuantities
        self.grid = self.new_grid()
        self.sweep = set()

    def new_grid(self):
        grid = []
        for x in range(self.sizes):
            grid.append([])
            for y in range(self.sizes):
                grid[x].append(None)

        return grid


grid = MinesweeperGrid(10, 10)
print(grid.grid)
