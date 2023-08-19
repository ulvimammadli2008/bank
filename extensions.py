from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app import app
from flask_admin import Admin
from flask_login import UserMixin, LoginManager
from flask_admin.contrib.sqla import ModelView

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager()

admin = Admin(app, name='YeloBank', template_mode='bootstrap4')