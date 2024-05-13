from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.orm import validates
from sqlalchemy.ext.associationproxy import association_proxy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Sport(db.Model):

    __tablename__ = 'sports_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    representative = db.Column(db.String)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'representative': self.representative
        }
    

class Sandwich(db.Model):

    __tablename__ = 'sandwiches_table'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }