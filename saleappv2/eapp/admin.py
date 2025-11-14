from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from eapp.models import Product, Category
from eapp import db, app

ad = Admin(app=app, name="CELL PHONE S's Admin")
ad.add_view(ModelView(Category, db.session))
ad.add_view(ModelView(Product, db.session))