# modelos.py
from app import mongo

def init_db():
    mongo.db.players.create_index('name', unique=True)
    mongo.db.staff.create_index('name', unique=True)
    mongo.db.equipment.create_index('name', unique=True)
