from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

Blog = Flask(__name__)
Blog.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"
Blog.config['SECRET_KEY'] = "hfdsa9wyt30f"
bcrypt = Bcrypt(Blog)
login = LoginManager(Blog)