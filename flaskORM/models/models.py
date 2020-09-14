from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


## Many to Many Relationships

product = db.Table('products',
                    db.Column('emp_name', db.String(25), db.ForeignKey('person.emp_name')),
                    db.Column('technology', db.String(25), db.ForeignKey('technology.technology')),
                    db.Column('product', db.String(25)))

##  One to One & Many relationship

class Technology(db.Model):
    technology = db.Column(db.String(50), primary_key= True)
    website = db.Column(db.String(50))
    tech = db.relationship('Person', backref="technology", lazy = 'dynamic', secondary= product)

    # def __repr__(self):
    #     return self.website
    def __init__(self, technology, website):
        self.technology= technology
        self.website = website
    
class Person(db.Model):
    #id = db.Column(db.Integer, primary_key = True)
    emp_id = db.Column(db.Integer, unique = True)
    emp_name = db.Column(db.String(50), primary_key = True)
    emp_technology = db.Column(db.String(10),db.ForeignKey('technology.technology'))
    login = db.relationship('Login', backref="person", lazy="dynamic")

    # def __repr__(self):
    #     return self.emp_technology
    
    def __init__(self, emp_id, emp_name, emp_technology):
        self.emp_id= emp_id
        self.emp_name = emp_name
        self.emp_technology = emp_technology



class Login(db.Model):
    id = db.Column(db. Integer, primary_key = True)
    username = db.Column(db.String(25), db.ForeignKey("person.emp_name"))
    password = db.Column(db.String(25), nullable= True)









