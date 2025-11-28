from flask import Flask, render_template, request, redirect
from flask_login import login_user, logout_user, current_user
from werkzeug.utils import redirect
from eapp import app, dao, login
from eapp.dao import auth_user
import math


@app.route('/')
def index():
    products = dao.load_products(cate_id=request.args.get('category_id'),
                                 kw=request.args.get('kw'),
                                 page=int(request.args.get('page', 1)))

    return render_template('index.html',products=products,
                           pages=math.ceil(dao.count_products()/app.config["PAGE_SIZE"]))
                            #Làm tròn lên số trang

@app.route('/login')
def login_view():
    return render_template('login.html')

@app.route('/register')
def register_view():
    return render_template('register.html')

@app.route('/login', methods=['post'])
def login_process():
    username = request.form.get('username')
    password = request.form.get('password')
    user = auth_user(username=username, password=password)
    if user:
        login_user(user=user)

    next = request.args.get('next')
    return redirect(next if next else'/admin')

@app.route('/logout')
def logout_process():
    logout_user()
    return redirect('/login')


@login.user_loader
def load_user(id):
    return dao.get_user_by_id(id)

'''Response chung khi ở trang đăng nhập/đăng ký/trang chủ đều hiện các danh mục sp'''
@app.context_processor
def common_response():
    return {
        'categories': dao.load_categories()
    }

if __name__ == '__main__':
    from eapp import admin
    app.run(debug=True)
