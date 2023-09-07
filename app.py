from flask import render_template, Flask, request
from bmi import bmi
from emi import get_emi

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contact-us")
def contact():
    return render_template("contact-us.html")

@app.route('/calc/health/bmi', methods=['post', 'get'])
def bmi_calc():
    if request.method == 'GET':
        return render_template("bmi.html")
    elif request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        res = bmi(weight, height)
        return render_template("bmi.html", res=round(res, 2))


@app.route('/calc/wealth/emi', methods=['post', 'get'])
def emi_calc():
    if request.method == 'GET':
        return render_template("emi.html")
    elif request.method == 'POST':
        principal = float(request.form['principal'])
        rate_of_interest = float(request.form['rate_of_interest'])
        no_of_years = int(request.form['no_of_years'])
        emi, comp = get_emi(principal, no_of_years, rate_of_interest)
        return render_template("emi.html", emi=emi, comp=comp)


if __name__ == '__main__':
    app.run(debug=True)
