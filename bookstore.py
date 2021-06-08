from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from database import db_session
import routes.book as BookRoute
import routes.cart as CartRoute
import routes.category as CategoryRoute
#tirar o model depois
from models.books import BooksModel
from models.cart import CartModel
from models.category import CategoryModel

app = Flask(__name__)

CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/bookstore_api"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db_session.app = app
db_session.init_app(app)

migrate = Migrate(app, db_session)

#add both routes(cart and crud book)
BookRoute.init_app(app)
CartRoute.init_app(app)
CategoryRoute.init_app(app)




