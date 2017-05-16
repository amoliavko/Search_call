from flask_wtf import FlaskForm
from wtforms.fields.html5 import DateField
from wtforms import StringField, TextField
from wtforms.validators import DataRequired, Required


class SearchCall(FlaskForm):
    data_from = StringField('Number', validators=[DataRequired()])
#    data_to = DateField('To', validators=[DataRequired()])
    data_to = DateField('To', validators=[DataRequired()])
    numb = StringField('Number', validators=[DataRequired()])
