from app import app
from flask import render_template
#nesse arquivo são definidas as rotas, nos importamos o app e aqui instauramos as rotas

@app.route('/')
def index():
    return render_template('index.html')

