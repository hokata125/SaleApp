from flask import Flask, render_template, request, redirect, jsonify, session
from flask_login import login_user, logout_user
from werkzeug.utils import redirect
from eapp import app, dao, login, utils
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

@app.route('/register', methods=['post'])
def register_process():
    password = request.form.get('password')
    confirmpass = request.form.get('confirmpass')
    if password != confirmpass:
        error_msg = 'Mật khẩu không khớp. Vui lòng kiểm tra lại!'
        return render_template('register.html', error_msg=error_msg)

    name = request.form.get('name')
    username = request.form.get('username')
    avatar = request.files.get('avatar')

    try:
        u = dao.add_user(name=name, username=username, password=password, avatar=avatar)
        return redirect('/login')
    except Exception as ex:
        return render_template('register.html', error_msg=str(ex))

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

@app.route('/api/carts', methods=['post'])
def add_to_cart():
    '''
        {
            "1", {
                "id": "1",
                "name": "aaaa",
                "price": 123,
                "quantity": 2
                },
            "2", {
                "id: "2",
                "name": "bbb",
                "price": 2234,
                "quantity": 1
                }
        }
    '''
    cart = session.get('cart')
    if not cart:
        cart = {}
    id = str(request.json.get("id"))
    if id in cart:
        cart[id]['quantity'] += 1
    else:
        name = request.json.get("name")
        price = request.json.get("price")
        cart[id] = {
            "id": id,
            "name": name,
            "price": price,
            "quantity": 1
        }
    session['cart'] = cart
    return jsonify({utils.stats_cart(cart)})

if __name__ == '__main__':
    from eapp import admin
    app.run(debug=True)
