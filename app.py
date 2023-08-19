from flask import Flask


app = Flask(__name__, template_folder='templates', static_folder="static")

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@localhost:3306/Yello_Bank"
app.config['SECRET_KEY'] = 'project'

from extensions import *
from controllers import *
from models import *
from forms import *





if __name__ == '__main__':
    db.init_app(db)
    db.init_app(migrate)
    app.run(port=5000, debug=True)


