from app.models import Cabana
from marshmallow import validate, fields, Schema, post_load


class CamabnaSchema(Schema):
    id = fields.Integer(dump_only=True)
    numero = fields.String(required=True)
    nombre = fields.String(required=True)
    capacidad = fields.Integer(required = True)

    @post_load
    def make_cabana(self,data, **kwargs):
        return Cabana(**data)