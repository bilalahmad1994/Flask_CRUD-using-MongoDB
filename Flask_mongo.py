from flask import Flask
from flask_pymongo import PyMongo
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

app.config['MONGO_DBNAME']='flaskmongo'
app.config['MONGO_URL'] = 'mongodb://bilalahmad1994:bilal1994@ds145148.mlab.com:45148/flaskmongo'
# print('this is console')
# print(app.config)

mongo=PyMongo(app)

connection = pymongo.MongoClient('ds145148.mlab.com', 45148)
db = connection['flaskmongo']
db.authenticate('bilalahmad1994','bilal1994')



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/add')
def add():
    user=db.users
    user.insert({'name': 'jawad', 'city': 'peshawar'})
    # user.insert({'name': 'ahmad', 'city': 'lahore'})
    # user.insert({'name': 'sami', 'city': 'lahore'})
    return 'Added User'

@app.route('/find')
def find():
    user = db.users
    sami = user.find_one({'name':'sami'})
    return 'his name is '+sami['name']+' language is '+sami['city']

@app.route('/update')
def update():
    user=db.users
    ahmad=user.find_one({'name':'ahmad'})
    ahmad['city']='karachi'
    user.save(ahmad)
    return 'updated '

@app.route('/delete')
def delete():
    user=db.user
    jawad=user.find_one({'name':'jawad'})
    user.remove(jawad)
    return 'removed jawad'



if __name__ == '__main__':
    app.run()