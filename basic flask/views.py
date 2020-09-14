from app import app
from flask import render_template,request


@app.route('/hello')
def mainpage():
    return render_template('basic.html')