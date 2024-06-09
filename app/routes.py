# routes.py
from flask import Blueprint, jsonify, request, render_template, redirect, url_for
from app import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/players', methods=['GET'])
def get_players():
    players = mongo.db.players.find()
    return render_template('players.html', players=players)

@main.route('/add_player', methods=['GET', 'POST'])
def add_player():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'position': request.form['position'],
            'number': request.form['number']
        }
        mongo.db.players.insert_one(data)
        return redirect(url_for('main.get_players'))
    return render_template('add_player.html')

@main.route('/staff', methods=['GET'])
def get_staff():
    staff = mongo.db.staff.find()
    return render_template('staff.html', staff=staff)

@main.route('/add_staff', methods=['GET', 'POST'])
def add_staff():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'role': request.form['role']
        }
        mongo.db.staff.insert_one(data)
        return redirect(url_for('main.get_staff'))
    return render_template('add_staff.html')

@main.route('/equipment', methods=['GET'])
def get_equipment():
    equipment = mongo.db.equipment.find()
    return render_template('equipment.html', equipment=equipment)

@main.route('/add_equipment', methods=['GET', 'POST'])
def add_equipment():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'quantity': request.form['quantity']
        }
        mongo.db.equipment.insert_one(data)
        return redirect(url_for('main.get_equipment'))
    return render_template('add_equipment.html')
