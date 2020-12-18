from flask import Flask, render_template, jsonify, request, make_response, redirect, url_for
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


@app.route('/search/<int:category>', methods=['POST'])
def search(category):
    if request.method == 'POST':
        keyword = request.form['ime']
        if category == 0:
            cafes = db.session.query(Coffee).filter_by(name=keyword)
            hospitals = db.session.query(Hospital).filter_by(name=keyword)
            banks = db.session.query(Bank).filter_by(name=keyword)
            offices = db.session.query(Office).filter_by(name=keyword)
            return render_template('search_results.html', cafes=cafes, hospitals=hospitals, banks=banks,
                                   offices=offices)
        elif category == 1:
            result = db.session.query(Coffee).filter_by(name=keyword)
            return render_template('search_results.html', data=result)
        elif category == 2:
            result = db.session.query(Bank).filter_by(name=keyword)
            return render_template('search_results.html', data=result)
        elif category == 3:
            result = db.session.query(Office).filter_by(name=keyword)
            return render_template('search_results.html', data=result)
        elif category == 4:
            result = db.session.query(Hospital).filter_by(name=keyword)
            return render_template('search_results.html', data=result)


@app.route('/search_banks', methods=['POST'])
def search_banks():
    pass


@app.route('/search_hospitals', methods=['POST'])
def search_hospitals():
    pass


@app.route('/search_offices', methods=['POST'])
def search_offices():
    pass


@app.route('/search_cafes', methods=['POST'])
def search_cafes():
    pass


@app.route('/banks/<int:id>', methods=['GET', 'POST'])
def bank(id):
    bank = db.session.query(Bank).filter_by(ID=id).first()
    if request.method == 'GET':
        return render_template('item.html', object=bank, back='banks')
    else:
        result = request.form['rating']
        bank.review = bank.review + int(result)
        db.session.commit()
        return render_template('item.html', object=bank, back='banks')


@app.route('/offices/<int:id>', methods=['GET', 'POST'])
def office(id):
    office = db.session.query(Office).filter_by(ID=id).first()
    if request.method == 'GET':
        return render_template('item.html', object=office, back='offices')
    else:
        result = request.form['rating']
        office.review = office.review + int(result)
        db.session.commit()
        return render_template('item.html', object=office, back='offices')


@app.route('/hospitals/<int:id>', methods=['GET', 'POST'])
def hospital(id):
    hospital = db.session.query(Hospital).filter_by(ID=id).first()
    if request.method == 'GET':
        return render_template('item.html', object=hospital, back='hospitals')
    else:
        result = request.form['rating']
        hospital.review = hospital.review + int(result)
        db.session.commit()
        return render_template('item.html', object=hospital, back='hospitals')


@app.route('/cafes/<int:id>', methods=['GET', 'POST'])
def cafe(id):
    cafe = db.session.query(Coffee).filter_by(ID=id).first()
    if request.method == 'GET':
        return render_template('item.html', object=cafe, back='coffees')
    else:
        result = request.form['rating']
        cafe.review = cafe.review + int(result)
        db.session.commit()
        return render_template('item.html', object=cafe, back='coffees')
