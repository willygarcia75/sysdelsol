from dataclasses import dataclass
from datetime import datetime
from flask_marshmallow import Schema
from app import db


@dataclass
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id:int = db.Column('id',db.Integer, primary_key = True, autoincrement = True)
    apellido : str = db.Column('apellido',db.String(50))
    nombre : str = db.Column('nombre',db.String(50))
    dni : int = db.Column('dni', db.Integer)
    email : str = db.Column('email', db.String(50))
    telefono : str = db.Column('telefono', db.String(15))
    direccion : str = db.Column('direccion', db.String(50))
    password : str = db.Column('password', db.Strin(64))




