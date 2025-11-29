import cloudinary
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'osgcxsh@!#$%^&*kncmagsnsphdhchapa@!#$%^&*aoeui'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 8

db = SQLAlchemy(app=app)
login = LoginManager(app=app)
cloudinary.config(
    cloud_name='dcf2a9fhh',
    api_key='717698739818743',
    api_secret='oju9J_Lznf_6wUbTT7tEkGbV7dQ'
)#về sửa lại sau