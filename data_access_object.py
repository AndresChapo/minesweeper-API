from config import db
from models import Grids
from minesweeper.MinesweeperGrid import MinesweeperGrid


def Grid_to_Minesweeper(db_grid):  # It gets a db_grid model and return a MinesweeperGrid
    game_grid = MinesweeperGrid(5, 1)
    game_grid.sizes = int(db_grid.sizes)
    game_grid.mines_cuantities = int(db_grid.mines_cuantities)
    game_grid.grid = db_grid.grid # must be a list of lists
    game_grid.swept = db_grid.swept # must be a set()
    game_grid.game_status = int(db_grid.game_status)
    return game_grid

def MinesweeperGrid_to_Grid(minesweeper_grid, id_game):  # It gets a MinesweeperGrid and return a db_grid model
    db_grid = Grids(1, 1, 1, [1], '(2,2)', 1)
    db_grid.id_game = int(id_game)
    db_grid.sizes = int(minesweeper_grid.sizes)
    db_grid.mines_cuantities = int(minesweeper_grid.mines_cuantities)
    db_grid.grid = minesweeper_grid.grid
    db_grid.swept = minesweeper_grid.swept
#    db_grid.swept = "{" + ",".join(map(str, minesweeper_grid.swept)) + "}" # Deprecated
    db_grid.game_status = int(minesweeper_grid.game_status)
    return db_grid

def persist_new_grids(game_grid):
    last_grid = db.session.query(Grids).order_by(Grids.id_game.desc()).first()
    new_grid_id = last_grid.id_game + 1

    db_grid = MinesweeperGrid_to_Grid(game_grid, new_grid_id)
    db.session.add(db_grid)
    db.session.commit()
    return db_grid

def get_one_grid(grid_id):
    db_grid = Grids.query.filter(Grids.id_game == grid_id).one_or_none()
    return db_grid

def update_grid(grid_id, game_grid):
    db_grid = Grids.query.filter(Grids.id_game == grid_id).one_or_none()
    if db_grid is not None:
        db_grid = Grids(id_game=grid_id, sizes=game_grid.sizes, mines_cuantities=game_grid.mines_cuantities,
              grid=game_grid.grid, swept=game_grid.swept, game_status=game_grid.game_status)
        db.session.merge(db_grid)
        db.session.commit()
    return db_grid
