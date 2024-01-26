from flask import Flask

#nesse arquivo teremos configurações do nosso app, e tudo que se relaciona com ele.

app = Flask(__name__)
app.config.from_object('config')


#importando as rotas que irá compor o app
from controllers import routes