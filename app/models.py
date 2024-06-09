from app import mongo

class Player:
    def __init__(self, name, position, number):
        self.name = name
        self.position = position
        self.number = number
        self.equipment = []

    def add_equipment(self, equipment):
        self.equipment.append(equipment)

    def remove_equipment(self, equipment):
        if equipment in self.equipment:
            self.equipment.remove(equipment)

    def save(self):
        mongo.db.players.insert_one({
            'name': self.name,
            'position': self.position,
            'number': self.number,
            'equipment': self.equipment
        })

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
