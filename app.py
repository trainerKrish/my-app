import sqlite3

from flask import render_template, Flask, request, session, redirect

from bmi import bmi
from emi import get_emi

app = Flask(__name__)


app.config['SECRET_KEY'] = 'my-secret-encoding'

conn = sqlite3.connect('db.sqlite3', check_same_thread=False)
cur = conn.cursor()
sql = """CREATE TABLE IF NOT EXISTS users (
    username VARCHAR(50) PRIMARY KEY,
    password VARCHAR(50),
    name VARCHAR(50)
)"""
cur.execute(sql)
conn.commit()
cur.close()


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    msg = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cur = conn.cursor()
        sql = f"select name, password FROM users WHERE username = '{username}'"
        cur.execute(sql)
        row = cur.fetchone()

        if row:
            if row[1] == password:
                msg = 'Login Successful'
                session['username'] = username
                session['name'] = row[0]
                return redirect('/')
            else:
                msg = 'Password is not matching'
        else:
            msg = 'User not exists, please register yourself'
        cur.close()

    return render_template("login.html", msg=msg)


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        pwd = request.form['password']
        print(request.form)
        cur = conn.cursor()
        sql = f"INSERT INTO users values ('{username}', '{pwd}', '{name}')"
        cur.execute(sql)
        conn.commit()
        cur.close()
        session['username'] = username
        session['name'] = name
        return redirect('/')

    return render_template("register.html")


@app.route("/logout")
def logout():
    session.clear()
    return render_template("home.html")


@app.route("/contact-us")
def contact():
    return render_template("contact-us.html")


@app.route('/calc/health/bmi', methods=['post', 'get'])
def bmi_calc():
    if 'username' not in session:
        return redirect('/login')

    if request.method == 'GET':
        return render_template("bmi.html")
    elif request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        res = bmi(weight, height)
        return render_template("bmi.html", res=round(res, 2))


@app.route('/calc/wealth/emi', methods=['post', 'get'])
def emi_calc():
    if 'username' not in session:
        return redirect('/login')

    if request.method == 'GET':
        return render_template("emi.html")
    elif request.method == 'POST':
        principal = float(request.form['principal'])
        rate_of_interest = float(request.form['rate_of_interest'])
        no_of_years = int(request.form['no_of_years'])
        emi, comp = get_emi(principal, no_of_years, rate_of_interest)
        return render_template("emi.html", emi=emi, comp=comp)


@app.route("/hero")
def hero():
    if 'username' not in session:
        return redirect('/login')

    return render_template("hero.html")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
