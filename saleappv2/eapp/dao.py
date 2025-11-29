import cloudinary.uploader
from eapp.models import Category, Product, User, UserRole
import hashlib
from eapp import app, db

def load_categories():
    return Category.query.all()

def load_products(cate_id=None, kw=None, page=1):
    query = Product.query

    if kw:
        query = query.filter(Product.name.contains(kw))
    if cate_id:
        query = query.filter(Product.category_id.__eq__(cate_id))
    if page:
        start = (page - 1) * app.config['PAGE_SIZE']
        query = query.slice(start, start + app.config['PAGE_SIZE'])

    return query.all()

def count_products():
    return Product.query.count()

def get_user_by_id(id):
    return User.query.get(id)

def auth_user(username, password):
    password=password=str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username==username.strip(),
                             User.password==password).first()

def add_user(name, username, password, avatar):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name=name.strip(), username=username.strip(), password=password, avatar=avatar)
    if avatar:
        res = cloudinary.uploader.upload(avatar)
        u.avatar = res.get('secret_url')
    db.session.add(u)
    try:
        db.session.commit()
    except Exception as ex:
        db.session.rollback()
        raise Exception('Tên đăng nhập đã tồn tại.')
