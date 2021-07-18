from minesweeper.MinesweeperGrid import MinesweeperGrid


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
        continue_game = True
        max_cuantities_of_sweeps = (self.grid.sizes * self.grid.sizes) - self.grid.mines_cuantities
        print("max_cuantities_of_sweeps ", max_cuantities_of_sweeps)

        while len(self.grid.swept) < max_cuantities_of_sweeps:
            # For debug
            print("holes_done ", len(self.grid.swept))
            print(str(self.grid.grid))
            print(str(self.grid.swept))
            # Real game
            print(self.grid)
            row = int(input("Row: "))
            column = int(input("Column: "))
            if self.validate_coordinates(row, column):
                continue_game = self.grid.sweep(row, column)
            else:
                print("Invalid coordinates!")
                continue
            if continue_game == False: break

        if continue_game:
            print("You Win!")
        else:
            for y in range(self.grid.sizes):
                for x in range(self.grid.sizes):
                    self.grid.swept.add((y, x))
            print(self.grid)
            print("Game Over!")


if __name__ == '__main__':
    game = Game()
    game.new_game(20, 20)
    game.run_on_console()
