from app import mongo
from bson.objectid import ObjectId

class Player:
    def __init__(self, name, position, number, equipment=None):
        self.name = name
        self.position = position
        self.number = number
        self.equipment = equipment

    def save(self):
        mongo.db.players.insert_one({
            'name': self.name,
            'position': self.position,
            'number': self.number,
            'equipment': self.equipment
        })

    @staticmethod
    def update_player(player_id, name, position, number, equipment):
        mongo.db.players.update_one(
            {'_id': ObjectId(player_id)},
            {'$set': {
                'name': name,
                'position': position,
                'number': number,
                'equipment': equipment
            }}
        )

    @staticmethod
    def find_player_by_id(player_id):
        return mongo.db.players.find_one_or_404({'_id': ObjectId(player_id)})

class Equipment:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def save(self):
        mongo.db.equipment.insert_one({
            'name': self.name,
            'quantity': self.quantity
        })

    @staticmethod
    def get_all():
        return list(mongo.db.equipment.find())

    @staticmethod
    def get_by_id(equipment_id):
        return mongo.db.equipment.find_one({'_id': equipment_id})

    @staticmethod
    def delete(equipment_id):
        mongo.db.equipment.delete_one({'_id': equipment_id})

    @staticmethod
    def update(equipment_id, name, quantity):
        mongo.db.equipment.update_one(
            {'_id': equipment_id},
            {'$set': {'name': name, 'quantity': quantity}}
        )

class Staff:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def save(self):
        mongo.db.staff.insert_one({
            'name': self.name,
            'role': self.role
        })

    @staticmethod
    def get_all():
        return list(mongo.db.staff.find())

    @staticmethod
    def get_by_id(staff_id):
        return mongo.db.staff.find_one({'_id': staff_id})

    @staticmethod
    def delete(staff_id):
        mongo.db.staff.delete_one({'_id': staff_id})

    @staticmethod
    def update(staff_id, name, role):
        mongo.db.staff.update_one(
            {'_id': staff_id},
            {'$set': {'name': name, 'role': role}}
        )
