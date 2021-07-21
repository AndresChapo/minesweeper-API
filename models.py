from flask import Flask, jsonify, request, make_response, abort
from flask_sqlalchemy import SQLAlchemy
from config import db, app


class Grids(db.Model):
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

""""
    def to_Grid(self, minesweeper_grid, id_game): # It gets a MinesweeperGrid and return a db_grid model
        self.id_game = id_game
        self.sizes = minesweeper_grid.sizes
        self.mines_cuantities = minesweeper_grid.mines_cuantities
        self.grid = minesweeper_grid.grid
        self.swept = minesweeper_grid.swept
        self.game_status = minesweeper_grid.game_status
        return self
"""
db.create_all()
db.session.commit()