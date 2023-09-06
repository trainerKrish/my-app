from flask import render_template, Flask, request
from bmi import bmi

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


    


if __name__ == '__main__':
    app.run(debug=True)
