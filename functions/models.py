from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    races = db.relationship('Race', backref='cup', lazy=True)

class Race(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    track = db.Column(db.String(120), nullable=False)
    cup_id = db.Column(db.Integer, db.ForeignKey('cup.id'), nullable=False)
    results = db.relationship('Result', backref='race', lazy=True)

class Racer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    is_user = db.Column(db.Boolean, default=False)
    results = db.relationship('Result', backref='racer', lazy=True)

class Result(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    race_id = db.Column(db.Integer, db.ForeignKey('race.id'), nullable=False)
    racer_id = db.Column(db.Integer, db.ForeignKey('racer.id'), nullable=False)
    finish_time = db.Column(db.Float, nullable=False)  # seconds
    position = db.Column(db.Integer, nullable=False)
    points = db.Column(db.Integer, nullable=False)

def init_db():
    db.create_all()
