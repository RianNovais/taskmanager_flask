from app import app, db
from flask import render_template, redirect, url_for, flash
from datetime import datetime
from models.forms import AddNewTaskForm, SearchTaskForm
from models.tables import Task

#Neste arquivo são definidas as rotas, importamos a aplicação e aqui instalamos as rotas
#In this file the routes are defined, we import the app and here we install the routes

@app.route('/')
def index():
    #aqui buscamos as tarefas, e mandamos pro template index.html, lá é inserido na determinada área de acordo com seu status
    #this is where we look for the tasks and send them to the index.html template, where they are inserted into a specific area according to their status
    tasks = Task.query.all()
    return render_template('index.html', tasks = tasks)

@app.route('/new_task', methods=['GET', 'POST'])
def new_task():
    form = AddNewTaskForm()
    if form.validate_on_submit():
        #valida quando o usuario clica no botão submit pega os dados inseridos no formulário lá no template, e adiciona no banco de dados e redireciona pra pagina inicial
        # #When the user clicks the submit button, it takes the data entered in the form in the template, adds it to the database and redirects to the home page.
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

@app.route('/remove_task', methods=['GET', 'POST'])
def remove_task():
    form = SearchTaskForm()

    #obtém o id do formulário quando o usuario clica no botão e verifica se existe uma tarefa com esse id, se existir ele remove a tarefa e redireciona pra pagina inicial
    #se nao existir exibe mensagem de erro!

    #get the id of the form when the user clicks on the button and check if there is a task with that id, if there is it removes the task and redirects to the home page
    #if it doesn't exist it displays an error message!

    if form.validate_on_submit():
        id = int(form.id.data)
        task = Task.query.filter_by(id = id).first()
        if not task:
            flash('Id task is invalid')
        else:
            print(task)
            db.session.delete(task)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('remove_task.html', form = form)

@app.route('/complete_task', methods=['GET', 'POST'])
def complete_task():
    # quando o usuario aperta o botão, verificamos se o id que ele escreveu correponde a alguma tarefa, se corresponder o status é modificado para "Completed"
    # when the user presses the button, we check if the id he wrote corresponds to any task, if it does the status is changed to "Completed"
    form = SearchTaskForm()

    if form.validate_on_submit():
        id = int(form.id.data)

        task = Task.query.filter_by(id = id).first()
        
        if not task:
            flash('id task is invalid')
        else:
            task.status = 'Completed'
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('complete_task.html', form = form)