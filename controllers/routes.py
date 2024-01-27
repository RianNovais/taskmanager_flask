from app import app
from flask import render_template

from models.forms import AddNewTaskForm

#In this file the routes are defined, we import the app and here we install the routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_task')
def new_task():
    form = AddNewTaskForm()
    return render_template('new_task.html', form = form)