from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

import shelve
app = Flask(__name__)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# login_manager = LoginManager(app)
# login_manager.login_view = 'login_page'
# never create login page yet don't enable login_manager yet

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
    return render_template('order.html')
@app.route('/settings')
def settings():
    return render_template('settings.html')
@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

@app.route('/CreateProduct')
def CreateProduct():
    return render_template('CreateProduct.html')

from shop import app

if __name__ == '__main__':
    app.run(debug=True)
