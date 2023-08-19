from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Length, Email

class Continue(FlaskForm):
    card_type = SelectField('Card Type', choices = [('', 'Card Type'), ('VISA', 'VISA'), ('Mastercard', 'Mastercard')], validators=[DataRequired()])
    currency = SelectField('Currency', choices = [('', 'Currency'), ('AZN', 'AZN'), ('USD', 'USD'), ('EUR', 'EUR')], validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    surname = StringField('Surname', validators=[DataRequired()])
    mobile_number = IntegerField('Mobile Number', validators=[DataRequired()])
    pin = StringField('PIN', validators=[DataRequired(), Length(min=7, max=7)])
    payment_methods = SelectField('Payment Methods', choices = [('', 'Payment Method'), ('price', 'With the payment of the card price'), ('deposit', 'With initial deposit')], validators=[DataRequired()])
    secret_word = StringField('Secret Word', validators=[DataRequired(), Length(min=1, max=7)])
    method_ac = SelectField('Method of acquisition', choices = [('', 'Method of acquisition'), ('Delivery', 'Delivery - Free'), ('branch', 'In bank branch')], validators=[DataRequired()])
    city = SelectField('City', choices = [('', 'City'), ('Baki', 'Baki')], validators=[DataRequired()])
    adress = StringField('Delivery Adress', validators=[DataRequired()])
    payment_type = SelectField('Payment type', choices = [('', 'Payment type'), ('Via', 'Via terminal')], validators=[DataRequired()]) 