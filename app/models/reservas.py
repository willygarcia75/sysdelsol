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
    
    
    # el tipo de pago va a estar en el 'pago'
    # tipopago: str = db.Column('Tipo de Pago', db.String(50))

    # agregar sólo cuando tengamos completas las partes del Schema y modelos
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    cliente = db.relationship("Cliente",foreign_keys = [cliente_id] )

    cabana_id = db.Column(db.Integer, db.ForeignKey('cabanas.id'))
    cabana = db.relationship("Cabana",foreign_keys = [cabana_id] )
 
 #  pago está vinculado al id de la reserva
 #   pago_id = db.Column(db.Ingeger, db.ForeignKey('pagos.id'))

