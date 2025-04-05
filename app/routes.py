# Contains all URL routes

from flask import Blueprint, render_template, request, redirect, url_for
from datetime import datetime
from .models import db, Habit

main = Blueprint('main', __name__)

@main.route('/')
def home():
    habits = Habit.query.all()
    return render_template('home.html', habits=habits)

@main.route('/add', methods=['GET', 'POST'])
def add_habit():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        new_habit = Habit(name=name, description=description)

        db.session.add(new_habit)
        db.session.commit()

        return redirect(url_for('main.home'))
    
    return render_template('add_habit.html')