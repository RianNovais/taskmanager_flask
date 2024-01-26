from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#nesse arquivo teremos configurações do nosso app, e tudo que se relaciona com ele.

app = Flask(__name__)
app.config.from_object('config')

#config db

db = SQLAlchemy(app)

#config migrate object pra realizar migrações

migrate = Migrate(app, db)

#importando as rotas que irá compor o app
from controllers import routes
#importando o model tables para migração
from models import tables