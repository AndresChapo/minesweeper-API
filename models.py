from flask import Flask, jsonify, request, make_response, abort
from flask_sqlalchemy import SQLAlchemy
import json
from sqlalchemy.ext.hybrid import hybrid_property
from config import db


class Grids(db.Model):
    __tablename__ = 'grids'
    id_game = db.Column(db.Integer(), primary_key=True)
    sizes = db.Column(db.Integer(), nullable=False)
    mines_cuantities = db.Column(db.Integer(), nullable=False)
    _grid = db.Column('grid', db.String(), nullable=False, default='[]')
    _swept = db.Column('swept', db.String(), nullable=False, default='[]')
    _flags = db.Column('flags', db.String(), nullable=False, default='[]')
    game_status = db.Column(db.Integer(), nullable=False, default=0)

    def __init__(self, id_game, sizes, mines_cuantities, grid, swept, game_status, flags):
        self.id_game = id_game
        self.sizes = sizes
        self.mines_cuantities = mines_cuantities
        self.grid = grid
        self.swept = swept
        self.flags = flags
        self.game_status = game_status

    @hybrid_property  # It's a getter
    def grid(self):
        return json.loads(self._grid)

    @grid.setter
    def grid(self, grid):
        self._grid = json.dumps(grid)  # Save it in a json friendly format

    @hybrid_property
    def swept(self):  # It's a getter
        list_of_list = json.loads(self._swept)
        return set(tuple(x) for x in list_of_list)  # Convert the list of list into a set of tuples

    @swept.setter
    def swept(self, swept):
        lista = list(list(x) for x in swept)  # Convert set with tuples into a list of list
        self._swept = json.dumps(lista)  # Save it in a json friendly format

    @hybrid_property
    def flags(self):  # It's a getter
        list_of_list = json.loads(self._flags)
        return set(tuple(x) for x in list_of_list)  # Convert the list of list into a set of tuples

    @flags.setter
    def flags(self, flags):
        lista = list(list(x) for x in flags)  # Convert set with tuples into a list of list
        self._flags = json.dumps(lista)  # Save it in a json friendly format


db.create_all()
db.session.commit()
