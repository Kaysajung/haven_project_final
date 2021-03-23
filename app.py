from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func



app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY'] = '_5#y2L"F4Q8z\n\xec]/'
db = SQLAlchemy(app)


@app.route('/',  methods = ['GET','POST'])
@app.route('/home',  methods = ['GET','POST'])
def home():
    return render_template('home.html')

@app.route('/aboutus',  methods = ['GET','POST'])
def aboutus():
    return render_template('aboutus.html')

@app.route('/cart',  methods = ['GET','POST'])
def cart():
    return render_template('cart.html')

@app.route('/contact',  methods = ['GET','POST'])
def contact():
    return render_template('contact.html')

@app.route('/currentevents',  methods = ['GET','POST'])
def currentevents():
    return render_template('currentevents.html')

@app.route('/davisleadership',  methods = ['GET','POST'])
def davisleadership():
    return render_template('davisleadership.html')

@app.route('/donate',  methods = ['GET','POST'])
def donate():
    return render_template('donate.html')

@app.route('/ndhsleadership',  methods = ['GET','POST'])
def ndhsleadership():
    return render_template('NDHSleadership.html')

@app.route('/pastevents',  methods = ['GET','POST'])
def pastevents():
    return render_template('pastevents.html')

@app.route('/pictures',  methods = ['GET','POST'])
def pictures():
    return render_template('pictures.html')

@app.route('/videos',  methods = ['GET','POST'])
def videos():
    return render_template('videos.html')


