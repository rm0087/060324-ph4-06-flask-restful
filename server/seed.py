#!/usr/bin/env python3

from app import app
from models import db, Sport
from faker import Faker

faker = Faker()

if __name__ == '__main__':
    with app.app_context():
        print("Seeding database...")

        Sport.query.delete()

        s1 = Sport(name="Extreme Yodeling")
        s2 = Sport(name="Ultimate Fridge Tossing")
        s3 = Sport(name="Freestyle Trash Diving")

        db.session.add_all([s1, s2, s3])
        db.session.commit()

        print("Seeding complete!")
