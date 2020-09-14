# from flask import Flask, render_template,request
# from flask_restful import Api, Resource

# app = Flask(__name__,static_url_path='', static_folder='static',template_folder='templates')
# api = Api(app)


# @app.route('/')
# def mainpage():
#     return render_template('basic.html')


# class Login(Resource):
#     def post(self):
#         data = request.form
#         return data
        
    
# api.add_resource(Login, '/login', endpoint = "Login")

# if __name__ == "__main__":
#     app.run(port = '5002')


from flask import Flask

app = Flask(__name__)
from views import *



if __name__ == "__main__":
    app.run(port = '5002')