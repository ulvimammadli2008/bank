from extensions import *
from flask_login import current_user
from app import app

class Cards(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable = True)
    subtitle = db.Column(db.String(255), nullable = True)
    term = db.Column(db.String(255), nullable = True)
    currency = db.Column(db.String(255), nullable = True)
    image = db.Column(db.String(255), nullable = True)
    cashback = db.Column(db.String(255), nullable = True)
    status = db.Column(db.Boolean, default=True)
    img = db.Column(db.String(255), nullable = True)
    title_i = db.Column(db.String(255), nullable = True)
    cashback_i = db.Column(db.String(255), nullable = True)
    delivery = db.Column(db.String(255), nullable = True)
    price = db.Column(db.String(255), nullable = True)
    cashback_categories =  db.Column(db.String(255), nullable = True)
    balance = db.Column(db.String(255), nullable = True)
    cashback_partners = db.Column(db.String(255), nullable = True)
    market = db.Column(db.String(255), nullable = True)
    market_per = db.Column(db.String(255), nullable = True)
    clothing = db.Column(db.String(255), nullable = True)
    clothing_per = db.Column(db.String(255), nullable = True)
    gas = db.Column(db.String(255), nullable = True)
    gas_per = db.Column(db.String(255), nullable = True)
    cafes = db.Column(db.String(255), nullable = True)
    cafes_per = db.Column(db.String(255), nullable = True)
    additional_information_title = db.Column(db.String(255), nullable = True)
    additional_information_subtitle = db.Column(db.String(500), nullable = True)
    


    def __repr__(self):
        return self.title, self.subtitle, self.term, self.currency, self.image, self.cashback, self.title_i, self.img, self.cashback_i, self.delivery, self.price, self.cashback_categories, self.balance, self.cashback_partners ,self.market, self.market_per, self.clothing, self.clothing_per, self.gas, self.gas_per, self.cafes, self.cafes_per, self.additional_information_title, self.additional_information_subtitle
    
    def __init__(self, title, subtitle, term, currency, image, cashback, title_i, img ,cashback_i, delivery, price, cashback_categories, balance, cashback_partners, market, market_per, clothing, clothing_per, gas, gas_per, cafes, cafes_per, additional_information_title, additional_information_subtitle, status):
        self.title = title
        self.subtitle = subtitle
        self.term = term
        self.currency = currency
        self.image = image
        self.cashback = cashback
        self.status = status
        self.title_i = title_i
        self.img = img
        self.cashback_i = cashback_i
        self.delivery = delivery
        self.price = price
        self.cashback_categories = cashback_categories
        self.balance = balance
        self.cashback_partners = cashback_partners
        self.market = market
        self.market_per = market_per
        self.clothing = clothing
        self.clothing_per = clothing_per
        self.gas = gas
        self.gas_per = gas_per
        self.cafes = cafes
        self.cafes_per = cafes_per
        self.additional_information_title = additional_information_title
        self.additional_information_subtitle = additional_information_subtitle
    
    def save(self):
        db.session.add(self)
        db.session.commit()



class Form_Sub(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    card_type = db.Column(db.String(255), nullable = True)
    currency = db.Column(db.String(255), nullable = True)
    name = db.Column(db.String(255), nullable = True)
    surname = db.Column(db.String(255), nullable = True)
    mobile_number = db.Column(db.Integer, nullable = True)
    pin = db.Column(db.String(255), nullable = True)
    payment_methods = db.Column(db.String(255), nullable = True)
    secret_word = db.Column(db.String(255), nullable = True)
    method_ac = db.Column(db.String(255), nullable = True)
    city = db.Column(db.String(255), nullable = True)
    adress = db.Column(db.String(255), nullable = True)
    type = db.Column(db.String(255), nullable = True)

    def __repr__(self):
        self.card_type, self.currency, self.name, self.surname, self.mobile_number, self.pin, self.payment_methods, self.secret_word, self.method_ac, self.city, self.adress, self.type

    def __init__(self, card_type, currency, name, surname, mobile_number, pin, payment_methods, secret_word, method_ac, city, adress, type):
        self.card_type = card_type
        self.currency = currency
        self.name = name
        self.surname = surname
        self.mobile_number = mobile_number
        self.pin = pin
        self.payment_methods = payment_methods
        self.secret_word = secret_word
        self.method_ac = method_ac
        self.city = city
        self.adress = adress
        self.type = type

    def save(self):
        db.session.add(self)
        db.session.commit()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(128))
    is_active = db.Column(db.Boolean, nullable=False)
    is_superuser = db.Column(db.Boolean, nullable=False)

    def init(self, id, username, password, is_active=True, is_superuser=False):
        self.id = id
        self.username = username
        self.password = password
        self.is_superuser = is_superuser
        self.is_active = is_active

    def get_id(self):
        return str(self.id)

    def save(self):
        db.session.add(self)
        db.session.commit()


def init_login():
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        if(user_id == "1"):
            return User(id=1,username="admin",password="123456")
        else :
            return False

class MyModelView(ModelView):

    def is_accessible(self):
        return current_user.is_active and current_user.id == 1
    


admin.add_view(MyModelView(Cards, db.session))


class Stories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable = True)
    link = db.Column(db.String(255), nullable = True)
    data = db.Column(db.String(255), nullable = True)
    status = db.Column(db.Boolean, default=True)

    def __repr__(self):
        self.title, self.link, self.data

    def __init__(self, title, link, data, status):
        self.title = title
        self.link = link
        self.data = data
        self.status = status

    def save(self):
        db.session.add(self)
        db.session.commit()


init_login()
admin.add_view(MyModelView(Stories, db.session))
