from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from init import config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "%s%s" % ('postgresql://', config.DB_CONNECT_STR)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Batch(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    file_in = db.Column('file_in', db.String)
    file_out = db.Column('file_out', db.String)
    datetime = db.Column('datetime', db.DateTime, default=datetime.now())
    status = db.Column('status', db.String, default='OK')


class Task(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    url = db.Column('url', db.String)
    status = db.Column('status', db.String)
    batch__oid = db.Column('batch__oid', db.Integer, db.ForeignKey('batch.id'), nullable=False)
    batch = db.relationship('Batch', backref=db.backref('tasks', lazy=True))


db.create_all()
