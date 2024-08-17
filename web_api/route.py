#!/usr/bin/env python3

from models import storage
from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_all_data():
    return storage.all()

@app.route('/lostIds/')
def get_all_ids():
    return storage.all('IdCards')

@app.route('/lostId/<string:id>')
def get_lost_id_by_id(id):
    return storage.show('IdCards', id)


@app.route('/users/<string:id>')
def get_user_by_id(id):
    return storage.show('User', id)

@app.route('/users/')
def get_all_users():
    return storage.all('User')

app.run(host='0.0.0.0')
