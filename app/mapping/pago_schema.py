from app.models import Pago
from marshmallow import validate, fields, Schema, post_load
from datetime import datetime

class PagoSchema(Schema): 
    id = fields.Integer(dump_only = True)
    fechapago = fields.DateTime(required = True)
    monto = fields.Integer(required = True)
    tipopago = fields.String(required = True)
    reserva = fields.Nested("ReserervaSechema", only= ("id", "fechaini", "fechafin", "cliente_id"))
    # los .Nested es porque son una ForeignKei y los only es para que solamente envíe esos campos por la web al cliente
    
    @post_load
    def make_pago(self,data, **kwargs):
        return Pago(**data)
    

    ''' El atributo dump_only en Marshmallow se utiliza para indicar que un campo debe ser 
    ignorado durante la deserialización (es decir, durante la conversión de un formato serializado, como JSON,
    de vuelta a un objeto Python). En tu caso, id = fields.Integer(dump_only=True) indica que el campo id
      no se espera en los datos entrantes y no se incluirá en los datos salientes.

    Por otro lado, el atributo required se utiliza para indicar que un campo debe estar presente en los datos entrantes
    durante la deserialización. Si un campo marcado como required no está presente en los datos entrantes,
    Marshmallow generará un error de validación. En tu caso, 
    numero = fields.String(required=True), 
    nombre = fields.String(required=True) y 
    capacidad = fields.Integer(required=True) 
    indican que estos campos deben estar presentes en los datos entrantes'''
    
