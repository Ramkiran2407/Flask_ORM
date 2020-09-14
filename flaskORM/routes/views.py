
from flask_restful import Resource
from flask import session, request, make_response, jsonify
from models.models import *
import jwt 
from datetime import datetime,timedelta
from functools import wraps

secert_key = "Thisissecret"

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'message': ' Token missing!'})
        
        try:
            data = jwt.decode(token, secert_key)
        except:
            return jsonify({'message': 'Token is invalid'})

        return f(*args, **kwargs)

class LoginPage(Resource):


    def post(self):
        username = None
        login_details = request.form
        session['username'] = login_details['username']
        token = jwt.encode({'user' : login_details['username'], 'exp': datetime.utcnow() + timedelta(seconds = 35)}, secert_key )
        return jsonify ({'token': token.decode('UTF-8'), 'message': 'Logged in successfully'})
        
    def get(post):

        auth = request.authorization 
        
        if auth and auth.password == "password":
            
            tech = Technology.query.all()  #select all query
            print(tech)
            for a in tech:
                print(type(a))
            
            c = Technology.query.join(Person, Technology.technology == Person.emp_technology).join(Login, Login.username == Person.emp_name).all()
            print(c, "c")
            
            d = Technology.query.join(Person, Technology.technology == Person.emp_technology).filter_by(emp_id = 18260).first()
            print(d)
            
            b = Technology.query.get('java')
            print(b.website)

            ## filter(modelname.column == values)

            e = Person.query.all()
            print(e)

            f = Person.query.join(Technology, Technology.technology == Person.emp_technology).add_columns(Technology.website).all()
            print(f)

            g = Person.query.order_by(Person.emp_id).limit(1).all()
            print(g)
            return "get with authentication"

        return make_response('could you verify', 401, {'WWW-Authenticate': 'basic real="Login required"'})