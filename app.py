from flask import Flask, jsonify, request, make_response, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from config import db, app
from minesweeper.Game import Game
from models import Grids
from data_access_object import *


# from minesweeper.MinesweeperGrid import MinesweeperGrid


@app.route("/")
def home():
    return render_template("game.html")


@app.route("/game")
def game():
    return render_template("game.html")


@app.route('/test', methods=['GET'])
def test():
    return {
        'test': 'test1'
    }


@app.route('/game/new/<int:sizes>/<int:mines>', methods=['GET'])
def get_game_new(sizes="", mines=""):
    #   new_game = request.get_json()
    output = []
    game = Game()
    grid = game.new_game_persist(sizes, mines)
    output.append(put_grid_in_directory(grid))
    return jsonify(output)


@app.route('/game/play/<int:grid_id>/<int:row>/<int:column>/<int:flag>', methods=['PUT'])
def put_game_play(grid_id="", row="", column="", flag=""):
    #    new_game = request.get_json()
    output = []
    game = Game()
    game.play_on_this_grid(grid_id, row, column, flag)
    output.append(put_grid_in_directory(get_one_grid(grid_id)))
    return jsonify(output)


@app.route('/grids', methods=['GET'])
@app.route('/grids/<int:grid_id>', methods=['GET'])
def get_grids(grid_id=""):
    output = []
    if grid_id == "":
        allGrids = Grids.query.all()
        for grid in allGrids:
            output.append(put_grid_in_directory(grid))
    else:
        grid = Grids.query.filter(Grids.id_game == grid_id).one_or_none()
        if grid is not None:
            output.append(put_grid_in_directory(grid))
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
        grid = Grids(id_game=gridData['id_game'], sizes=gridData['sizes'],
                     mines_cuantities=gridData['mines_cuantities'],
                     grid=gridData['grid'], swept=gridData['swept'], game_status=gridData['game_status'])
        db.session.merge(grid)
        db.session.commit()
        return make_response(
            "Grid {grid_id} updated".format(grid_id=grid_id), 200
        )
    else:
        abort(
            404,
            "Grid not found for Id: {grid_id}".format(grid_id=grid_id)
        )


""""
@app.route('/grids', methods=['POST'])
def post_grids(): # Probably it will be deprecated, because you shouldn't be able to create a grid from de API/frontend. It's a Game class responsability.
    gridData = request.get_json()

#    game_grid = MinesweeperGrid()

    persist_new_grids(game_grid)
    return jsonify(gridData)


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
