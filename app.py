from flask import Flask, request ,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os


# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db = SQLAlchemy(app)
ma = Marshmallow(app)

@app.before_first_request
def create_tables():
    db.create_all()

class Details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100),unique=True)
    description = db.Column(db.String(200))
    types = db.Column(db.String(100))
    age = db.Column(db.Integer)  
    datetime= db.Column(db.String(100))

    def __init__(self,name,types,description,age,datetime):
        self.name = name
        self.description = description
        self.age= age
        self.datetime = datetime
        self.types = types

class DetailSchema(ma.Schema):
    class Meta:
        fields =('id','name','description','age','types','datetime')
    

detail_schema = DetailSchema()
details_schema = DetailSchema()

# Create Detail of a person
@app.route('/add_detail',methods=['POST'])
def add_details():
    name = request.json['name']   
    age = request.json['age']   
    types = request.json['types']   
    datetime = request.json['datetime']   
    description  = request.json['description']      

    new_person = Details(name,age,types,description,datetime)

    db.session.add(new_person)
    db.session.commit()

    return detail_schema.jsonify(new_person)


# Get All Person details 
@app.route('/all_details', methods=['GET'])
def get_all_details():
  all_details = Details.query.all()
  result = details_schema.dump(all_details)
  return jsonify(result)

# Get Single Person details 
@app.route('/details/<id>', methods=['GET'])
def get_single_detail(id):
  detail = Details.query.get(id)
  return detail_schema.jsonify(detail)

# Update a Person details 
@app.route('/update_details/<id>', methods=['PUT'])
def update_product(id):
  detail = Details.query.get(id)

  name = request.json['name']
  age = request.json['age']   
  types = request.json['types']   
  datetime = request.json['datetime']   
  description  = request.json['description']      

  detail.name = name
  detail.description = description
  detail.age = age
  detail.types = types
  detail.datetime = datetime

  db.session.commit()

  return detail_schema.jsonify(detail)

# Delete Person details 
@app.route('/delete_details/<id>', methods=['DELETE'])
def delete_product(id):
  detail = Details.query.get(id)
  db.session.delete(detail)
  db.session.commit()

  return detail_schema.jsonify(detail)

# Run Server
if __name__ == '__main__':
    app.run(debug=True)