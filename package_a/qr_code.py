from peewee import CharField, DateTimeField, IntegerField

from .db import db


class QrCode(db.Model):
    code = CharField(null=True)
    created_on = DateTimeField(null=True)
    legacy = IntegerField()

    class Meta:
        table_name = "qr"
