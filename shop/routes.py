from shop import app
from flask import render_template, request, redirect, url_for
from .Forms import CreateOrderForm
import shelve
from .Order import Order
# from flask_login import login_user, logout_user
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/about_us')
def about_us_page():
    return render_template('aboutUs.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/forgot_password')
def forgot_password_page():
    return render_template('forgot_password.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/order')
def order():
    order_dict= {}
    db = shelve.open('order.db','r')
    order_dict = db['Orders']
    db.close()

    order_list = []
    for key in order_dict:
        order = order_dict.get(key)
        order_list.append(order)

    return render_template('order.html', count=len(order_list), order_list =order_list)

@app.route('/orderform', methods=['GET','POST'])
def orderform():
    create_order_form=CreateOrderForm(request.form)
    if request.method == 'POST' and create_order_form.validate():
        order_dict = {}
        db = shelve.open('order.db', 'c')

        try:
            order_dict = db['Orders']
        except:
            print("Error in retrieving Users from order.db.")

        order = Order(create_order_form.first_name.data, create_order_form.last_name.data, create_order_form.gender.data, create_order_form.membership.data, create_order_form.remarks.data)
        order_dict[order.get_order_id()] = order
        db['Orders'] = order_dict
        return redirect(url_for('order'))
    return render_template('orderform.html', form=create_order_form)

@app.route('/deleteOrder/<int:id>', methods=['POST'])
def delete_order(id):
    order_dict = {}
    db = shelve.open('order.db', 'w')
    order_dict = db['Orders']

    order_dict.pop(id)

    db['Order'] = order_dict
    db.close()

    return redirect(url_for('order'))

@app.route('/settings')
def settings():
    return render_template('settings.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

