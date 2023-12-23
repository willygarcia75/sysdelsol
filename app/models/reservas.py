from dataclasses import dataclass
from datetime import datetime
from flask_marshmallow import Schema
from app import db


@dataclass
class Reserva(db.Model):
    __tablename__ = 'reservas'
    id:int = db.Column('id',db.Integer, primary_key = True, autoincrement = True)
    fechaini: datetime = db.Column('fecha de inicio', db.DateTime(), nullable = False)
    fechafin: datetime = db.Column('fecha de finalizacion', db.DateTime())
    tipopago: str = db.Column('Tipo de Pago', db.String(50))

    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    pago_id = db.Column(db.Ingeger, db.ForeignKey('pagos.id'))

