from dataclasses import dataclass
from datetime import datetime
from flask_marshmallow import Schema
from app import db


@dataclass
class Pago(db.Model):
    __tablename__ = 'pagos'
    
    id:int = db.Column('id',db.Integer, primary_key = True, autoincrement = True)
    reserva_id : int = db.Column('reserva_id', db.Integer)
    # apellido : str=db.Column('apellido',db.String(50)) # bla
    fechapago: datetime = db.Column('fecha de pago', db.DateTime(), default = datetime.utcnow)
    
    monto: int = db.Column('monto', db.Integer())
    # los montos se guardan en centavos para mayor precision.... ojo al hacer los carteles debe dividirse por 100 para 
    # mostrar los pesos

    # 
    tipopago: str = db.Column('tipopago', db.String(50), nullable = False)

    reserva_id = db.Column(db.Integer, db.ForeignKey('reservas.id'))
    reserva = db.relationship("Reserva",foreign_keys = [reserva_id] )