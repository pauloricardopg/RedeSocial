import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import sqlalchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '46ca2defb01cc7f0b122f36e6ca22e9d'


base_dir = os.path.abspath(os.path.dirname(__file__))
url = os.getenv("DATABASE_URL")


if url and url.startswith("postgres://"):
    url = url.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = url or f'sqlite:///{os.path.join(base_dir, "comunidade.db")}'


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Para acessar essa página você precisa estar logado'
login_manager.login_message_category = 'alert-info'


from comunidadeimpressionadora import models
with app.app_context():
    engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
    inspector = sqlalchemy.inspect(engine)
    if not inspector.has_table("usuario"):
        database.create_all()
        print("✅ Banco de dados criado com sucesso!")
    else:
        print("✅ Banco de dados já existente.")

from comunidadeimpressionadora import routes
