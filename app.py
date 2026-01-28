import sqlite3
from flask import Flask, render_template, g

from pprint import pprint

app = Flask(__name__)
app.config['DEBUG'] = True
DATABASE = './liminal_krk.db'

# TODO We'll need to port this to MySQL... Target env uses it
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
        with open('liminal_krk.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET'])
def get_index():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM place')
    places = cursor.fetchall()
    print(places)
    return render_template('index.html', places=places)

@app.route('/place/<int:id>', methods=['GET'])
def get_place(id):
    db = get_db()
    items = db.execute(f'SELECT * FROM item WHERE place_id = {id}').fetchall()
    place = db.execute(f'SELECT * FROM place WHERE id = {id}').fetchone()
    return render_template('place.html', place=place, items=items)

def create_app():
    return app
