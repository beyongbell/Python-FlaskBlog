from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import DefaultMeta, Model

flask_blog = Flask(__name__)
flask_blog.config['SECRET_KEY'] = 'd42f7b60fad9c6c81f2d3c4b48650844'
flask_blog.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(flask_blog)

from app import routes