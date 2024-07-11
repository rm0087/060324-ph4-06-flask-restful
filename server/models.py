from config import db
from sqlalchemy_serializer import SerializerMixin


class Sport(db.Model, SerializerMixin):

    __tablename__ = 'sports_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)