from flask import Flask, render_template, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dataset.db'

db = SQLAlchemy(app)

db.reflect()  # reflection to get table meta


class Hospital(db.Model):
    __tablename__ = 'hospital'


class Bank(db.Model):
    __tablename__ = 'bank'


class Coffee(db.Model):
    __tablename__ = 'coffee'


class Office(db.Model):
    __tablename__ = 'coffee'


@app.route('/')
def index():
    results = db.session.query(Office).all()
    return render_template('index.html', data=results)


@app.route('/offices')
def offices():
    results = db.session.query(Office).all()
    return render_template('offices.html', data=results)


@app.route('/hospitals')
def hospitals():
    results = db.session.query(Hospital).all()
    return render_template('hospital.html', data=results)


@app.route('/coffees')
def coffees():
    results = db.session.query(Coffee).all()
    return render_template('cafe.html', data=results)


@app.route('/banks')
def banks():
    results = db.session.query(Bank).all()
    return render_template('Banks.html', data=results)
