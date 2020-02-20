from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class BestResaleForm(FlaskForm):
    target_annual_milage = StringField('Annual Milage', [DataRequired()])
    submit = SubmitField('Search Cars')

class InDepthSearch(FlaskForm):
    pass