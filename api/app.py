from flask import Flask, jsonify, request, make_response, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgresql@localhost:5433/testbd'
# password admin200
app.debug = True
db = SQLAlchemy(app)


class grids(db.Model):
    __tablename__ = 'grids'
    id_game = db.Column(db.Integer(), primary_key=True)
    sizes = db.Column(db.Integer(), nullable=False)
    mines_cuantities = db.Column(db.Integer(), nullable=False)
    grid = db.Column(db.String(), nullable=False)
    swept = db.Column(db.String(), nullable=False)
    game_status = db.Column(db.Integer(), nullable=False, default=0)

    def __init__(self, id_game, sizes, mines_cuantities, grid, swept, game_status):
        self.id_game = id_game
        self.sizes = sizes
        self.mines_cuantities = mines_cuantities
        self.grid = grid
        self.swept = swept
        self.game_status = game_status


db.create_all()
db.session.commit()


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
        allGrids = grids.query.all()
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
        grid = grids.query.filter(grids.id_game == grid_id).one_or_none()
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


if __name__ == '__main__':
    app.run()
