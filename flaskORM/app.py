from flask import Flask, render_template, session, request, redirect, g
from models.models import db
from flask_restful import Api
from datetime import timedelta
import jwt


app = Flask(__name__, static_url_path = "", template_folder = "templates", static_folder = "static")
api = Api(app)
database_file = "mysql://root:root@localhost/queries"   
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.secret_key = "any"
app.permanent_session_lifetime = timedelta(seconds=35)

db.init_app(app)


with app.app_context():
    db.create_all()


@app.route('/')
def sample():
    username = None 
    if 'username' in session:
        username = session['username']
        return redirect('/login')
    return render_template("photography.html")

from routes.views import LoginPage


api.add_resource(LoginPage, '/login', endpoint = "LoginPage")

if __name__ == "__main__":
    app.run()