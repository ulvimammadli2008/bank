from flask import render_template, request, redirect, url_for
from app import app
from wtforms import *
from forms import *
from models import Cards, Form_Sub, User, Stories
from flask_login import login_user, logout_user


@app.route('/main/')
def main():
    each_story = Stories.query.filter_by(status = True).all()
    return render_template('main.html', each = each_story) 

@app.route('/story/')
def story():
    # each = Stories.query.filter_by(id = id).first()
    return render_template('story.html')
# story_each = each


@app.route('/cards/')
def cards():
    each_card = Cards.query.filter_by(status = True).all()
    return render_template('cards.html', each_card_h = each_card)


@app.route('/card/<int:id>/', methods = ['GET', 'POST'])
def card(id):
    each = Cards.query.filter_by(id = id).first()
    all_data = request.form
    form = Continue(data=all_data)
    if request.method == 'POST':
        if form.validate_on_submit():
            form_sub_s = Form_Sub(card_type=form.card_type.data, name= form.name.data, surname=form.surname.data, currency=form.currency.data, mobile_number=form.mobile_number.data, pin=form.pin.data, payment_methods=form.payment_methods.data, secret_word=form.secret_word.data, method_ac=form.method_ac.data, city=form.city.data, adress=form.adress.data, type=form.payment_type.data)
            form_sub_s.save()
    return render_template('order.html', each_1 = each, form =form)


@app.route('/admin/login', methods = ['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'yelobank' and password == "123456":
            user = User(id=1, username='yelobank', password='123456')
            login_user(user)
            return redirect('/admin')
        else:
            return 'Bye'
    else:
        return render_template('index.html')
    

@app.route('/admin/logout', methods = ['GET'])
def admin_l():
    logout_user()
    return redirect('/admin/login')