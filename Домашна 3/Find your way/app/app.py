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


@app.route('/search', methods=['POST'])
def search():
    pass


@app.route('/banks/<int:id>',methods=['GET','POST'])
def bank(id):
    if request.method=='GET':
        bank = db.session.query(Bank).filter_by(ID=id).first()
        return render_template('item.html', object=bank, back='banks')
    else:
        return "To be implemented"


@app.route('/offices/<int:id>',methods=['GET','POST'])
def office(id):
    if request.method=='GET':
        office = db.session.query(Office).filter_by(ID=id).first()
        return render_template('item.html', object=office, back='offices')
    else:
        return "To be implemented"


@app.route('/hospitals/<int:id>',methods=['GET','POST'])
def hospital(id):
    if request.method=='GET':
        hospital = db.session.query(Hospital).filter_by(ID=id).first()
        return render_template('item.html', object=hospital, back='hospitals')
    else:
        return "To be implemented"


@app.route('/cafes/<int:id>',methods=['GET','POST'])
def cafe(id):
    if request.method=='GET':
        cafe = db.session.query(Coffee).filter_by(ID=id).first()
        return render_template('item.html', object=cafe, back='coffees')
    else:
        return "To be implementd"