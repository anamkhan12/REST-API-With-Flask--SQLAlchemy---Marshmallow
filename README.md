# REST-API-With-Flask-SQLAlchemy-Marshmallow
 In this project i have used Python Flask along with SQL Alchemy and Marshmallow to create a RESTful API to CRUD Details.
 
# Activate venv
$ pipenv shell

# Install dependencies
$ pipenv install

# Create DB
$ python
>> from app import db
>> db.create_all()
>> exit()

# Run Server (http://localhst:5000)
python app.py
