from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired


class BestResaleForm(FlaskForm):
    target_price = StringField('Target Price', [DataRequired()])
    target_annual_mileage = StringField('Annual Mileage', [DataRequired()])
    checkbox = BooleanField('Use User Data: ')
    submit = SubmitField('Search Cars')

class InDepthSearch(FlaskForm):
    car_make_model = StringField('Car Make', [DataRequired()])
    new_area = StringField('New Area', [DataRequired()])
    refresh = SubmitField('Refresh')

class RefreshForm(FlaskForm):
    new_area = StringField('New Area', [DataRequired()])
    owner_type = StringField('Owner Type', [DataRequired()])
    refresh = SubmitField('Refresh')