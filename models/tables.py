from app import db

#criação do modelo da tabela tasks que será migrada pro banco de dados


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String, nullable = False)
    priority = db.Column(db.String, nullable = False)
    status = db.Column(db.String, nullable = False)
    startDate = db.Column(db.String, nullable = False)

    def __init__(self, name, priority, status, startDate):
        self.name = name
        self.priority = priority
        self.status = status
        self.startDate = startDate


        




    
    