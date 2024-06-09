from flask import Blueprint, render_template, request, redirect, url_for
from bson.objectid import ObjectId
from app.models import Player, Equipment, Staff
from app import mongo

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

# Players routes
@main.route('/players', methods=['GET'])
def get_players():
    players = list(mongo.db.players.find())
    equipment = {str(item['_id']): item['name'] for item in mongo.db.equipment.find()}

    for player in players:
        player_equipment_id = str(player.get('equipment', ''))
        player['equipment_name'] = equipment.get(player_equipment_id, 'Unknown')

    return render_template('players.html', players=players)

@main.route('/players/add', methods=['GET', 'POST'])
def add_player():
    if request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        number = int(request.form['number'])
        player = Player(name, position, number)
        player.save()
        return redirect(url_for('main.get_players'))
    return render_template('add_player.html')

@main.route('/edit_player/<player_id>', methods=['GET', 'POST'])
def edit_player(player_id):
    if request.method == 'GET':
        player = Player.find_player_by_id(player_id)
        equipment = list(mongo.db.equipment.find())
        return render_template('edit_player.html', player=player, equipment=equipment)
    elif request.method == 'POST':
        name = request.form['name']
        position = request.form['position']
        number = request.form['number']
        equipment = request.form['equipment']

        Player.update_player(player_id, name, position, number, equipment)
        return redirect(url_for('main.get_players'))

@main.route('/players/delete/<string:player_id>', methods=['POST'])
def delete_player(player_id):
    mongo.db.players.delete_one({'_id': ObjectId(player_id)})
    return redirect(url_for('main.get_players'))

# Equipment routes
@main.route('/equipment', methods=['GET'])
def get_equipment():
    equipment = Equipment.get_all()
    return render_template('equipment.html', equipment=equipment)

@main.route('/equipment/add', methods=['GET', 'POST'])
def add_equipment():
    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form['quantity'])
        equipment = Equipment(name, quantity)
        equipment.save()
        return redirect(url_for('main.get_equipment'))
    return render_template('add_equipment.html')


@main.route('/equipment/edit/<string:equipment_id>', methods=['GET', 'POST'])
def edit_equipment(equipment_id):
    equipment = mongo.db.equipment.find_one_or_404({'_id': ObjectId(equipment_id)})
    
    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form['quantity'])
        
        mongo.db.equipment.update_one(
            {'_id': ObjectId(equipment_id)},
            {'$set': {'name': name, 'quantity': quantity}})
        
        return redirect(url_for('main.get_equipment'))
    
    return render_template('edit_equipment.html', equipment=equipment)

@main.route('/equipment/delete/<string:equipment_id>', methods=['POST'])
def delete_equipment(equipment_id):
    mongo.db.equipment.delete_one({'_id': ObjectId(equipment_id)})
    return redirect(url_for('main.get_equipment'))



# Staff routes
@main.route('/staff', methods=['GET'])
def get_staff():
    staff = Staff.get_all()
    return render_template('staff.html', staff=staff)

@main.route('/staff/add', methods=['GET', 'POST'])
def add_staff():
    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        staff = Staff(name, role)
        staff.save()
        return redirect(url_for('main.get_staff'))
    return render_template('add_staff.html')

@main.route('/staff/delete/<string:staff_id>', methods=['POST'])
def delete_staff(staff_id):
    Staff.delete(staff_id)
    return redirect(url_for('main.get_staff'))


@main.route('/staff/edit/<string:staff_id>', methods=['GET', 'POST'])
def edit_staff(staff_id):
    staff = Staff.get_by_id(staff_id)
    
    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        
        Staff.update(staff_id, name, role)
        
        return redirect(url_for('main.get_staff'))
    
    return render_template('edit_staff.html', staff=staff)
