from flask import Flask, jsonify, request, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from config import db, app
from models import Grids
from data_access_object import *
from minesweeper.MinesweeperGrid import MinesweeperGrid

@app.route('/test', methods=['GET'])
def test():
    return {
        'test': 'test1'
    }


@app.route('/grids', methods=['GET'])
@app.route('/grids/<int:grid_id>', methods=['GET'])
def get_grids(grid_id=""):
    output = []
    if grid_id == "":
        allGrids = Grids.query.all()
        for grid in allGrids:
            currGrid = {}
            currGrid['id_game'] = grid.id_game
            currGrid['sizes'] = grid.sizes
            currGrid['mines_cuantities'] = grid.mines_cuantities
            currGrid['grid'] = grid.grid
            currGrid['swept'] = grid.swept
            currGrid['game_status'] = grid.game_status
            output.append(currGrid)
    else:
        grid = Grids.query.filter(Grids.id_game == grid_id).one_or_none()
        if grid is not None:
            currGrid = {}
            currGrid['id_game'] = grid.id_game
            currGrid['sizes'] = grid.sizes
            currGrid['mines_cuantities'] = grid.mines_cuantities
            currGrid['grid'] = grid.grid
            currGrid['swept'] = grid.swept
            currGrid['game_status'] = grid.game_status
            output.append(currGrid)
        else:
            abort(
                404,
                "Grid not found for Id: {grid_id}".format(grid_id=grid_id)
            )
    return jsonify(output)

@app.route('/grids/update/<int:grid_id>', methods=['PUT'])
def put_grids(grid_id=""):
    gridData = request.get_json()
    grid = Grids.query.filter(Grids.id_game == grid_id).one_or_none()
    if grid is not None:
        grid = Grids(id_game=gridData['id_game'], sizes=gridData['sizes'], mines_cuantities=gridData['mines_cuantities'],
                     grid=gridData['grid'], swept=gridData['swept'], game_status=gridData['game_status'])
        db.session.merge(grid)
        db.session.commit()
        return make_response(
            "Grid {grid_id} updated".format(grid_id=grid_id),200
        )
    else:
        abort(
            404,
            "Grid not found for Id: {grid_id}".format(grid_id=grid_id)
        )

@app.route('/grids', methods=['POST'])
def post_grids(): # Probably it will be deprecated, because you shouldn't be able to create a grid from de API/frontend. It's a Game class responsability.
    gridData = request.get_json()

    game_grid = MinesweeperGrid()

    new_game_grids(game_grid)
    return jsonify(gridData)

""""
@app.route('/grids', methods=['POST'])
def post_grids():
    gridData = request.get_json()
    last_grid = db.session.query(Grids).order_by(Grids.id_game.desc()).first()
    new_grid_id = last_grid.id_game + 1
    grid = Grids(id_game=new_grid_id, sizes=gridData['sizes'], mines_cuantities=gridData['mines_cuantities'],
                 grid=gridData['grid'], swept=gridData['swept'], game_status=gridData['game_status'])
    db.session.add(grid)
    db.session.commit()
    return jsonify(gridData)
"""

@app.route('/grids/delete/<int:grid_id>', methods=['DELETE'])
def delete_books(grid_id=""):
    grid = Grids.query.filter(Grids.id_game == grid_id).one_or_none()
    if grid is not None:
        db.session.delete(grid)
        db.session.commit()
        return make_response(
            "Grid {grid_id} deleted".format(grid_id=grid_id), 200
        )
    else:
        abort(
            404,
            "Grid not found for Id: {grid_id}".format(grid_id=grid_id)
        )

if __name__ == '__main__':
    app.run()
