from flask import Flask
from flask_bcrypt import Bcrypt

Blog = Flask(__name__)
Blog.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///blog.db"
bcrypt = Bcrypt(Blog)