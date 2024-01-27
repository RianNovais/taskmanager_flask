from app import app
from flask import render_template, redirect, url_for
from datetime import datetime

from app import db
from models.forms import AddNewTaskForm
from models.tables import Task




#In this file the routes are defined, we import the app and here we install the routes

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new_task', methods=['GET', 'POST'])
def new_task():
    form = AddNewTaskForm()
    if form.validate_on_submit():
        #valida quando o usuario clica no botão submit pega os dados inseridos no formulário lá no template, e adiciona no banco de dados e redireciona pra pagina inicial
        
        nameTask = form.name.data
        descriptionTask = form.description.data
        startDateTask = datetime.strftime(form.startDate.data, '%d/%m/%Y')
        priorityTask = form.priority.data
        statusTask = form.status.data

        task = Task(nameTask, descriptionTask, priorityTask, statusTask, startDateTask)

        db.session.add(task)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('new_task.html', form = form)