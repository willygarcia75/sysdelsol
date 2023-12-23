from dataclasses import dataclass
from datetime import datetime
from flask_marshmallow import Schema
from app import db


@dataclass
class Pago(db.Model):
    __tablename__ = 'pagos'
    id:int = db.Column('id',db.Integer, primary_key = True, autoincrement = True)
    reserva_id : int
    fechapago: datetime = db.Column('fecha de pago', db.DateTime(), default = datetime.utcnow)
    monto: int = db.Column('monto', db.Integer())
    # los montos se guardan en centavos para mayor precision.... ojo al hacer los carteles

    tipopago: str = db.Column('Tipo de Pago', db.String(50), nullable = False)

