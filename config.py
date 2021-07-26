from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgresql@localhost:5433/testbd'
# password admin200
app.debug = True
db = SQLAlchemy(app)

# User: desperta_minesweeper
# Database: desperta_minesweeperbd
# pass: minesweeper