from config import db
from models import Grids
from minesweeper.MinesweeperGrid import MinesweeperGrid

def new_game_grids(game_grid):
    last_grid = db.session.query(Grids).order_by(Grids.id_game.desc()).first()
    new_grid_id = last_grid.id_game + 1
    db_grid = Grids(id_game=new_grid_id, sizes=game_grid.sizes, mines_cuantities=game_grid.mines_cuantities,
                 grid=game_grid.grid, swept=game_grid.swept, game_status=game_grid.game_status)
    db.session.add(db_grid)
    db.session.commit()
    return db_grid

def get_one_grid(grid_id):
    grid = Grids.query.filter(Grids.id_game == grid_id).one_or_none()
    # excetion            "Grid not found for Id: {grid_id}".format(grid_id=grid_id)
    return grid

def update_grid(grid_id,game_grid):
    db_grid = Grids.query.filter(Grids.id_game == grid_id).one_or_none()
    if db_grid is not None:
        db_grid = Grids(id_game=grid_id, sizes=game_grid.sizes, mines_cuantities=game_grid.mines_cuantities,
              grid=game_grid.grid, swept=game_grid.swept, game_status=game_grid.game_status)
        db.session.merge(db_grid)
        db.session.commit()
    return db_grid
