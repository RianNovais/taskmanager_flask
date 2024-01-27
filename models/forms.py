from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SelectField
from wtforms.validators import DataRequired

class AddNewTaskForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    startDate = DateField('startDate', validators=[DataRequired()])
    status = SelectField('status', choices=['Completed', 'In progress'], validators=[DataRequired()])
    priority = SelectField('status', choices=['High', 'Medium', 'Low'], validators=[DataRequired()])