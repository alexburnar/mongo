from flask import Flask
from flask.ext.pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'connect_to_mongo'
app.config['MONGO_URI'] = 'mongodb://pretty:uno12345@ds255463.mlab.com:55463/connect_to_mongo'


mongo = PyMongo(app)

@app.route('/add')
def add():
	user = mongo.db.users
	user.insert({'name': 'Anthony', 'language': 'python'})
	user.insert({'name': 'Jhon', 'language': 'c'})
	user.insert({'name': 'Anthony', 'language': 'python'})
	user.insert({'name': 'Jhon', 'language': 'c'})
	user.insert({'name': 'Anthony', 'language': 'python'})
	user.insert({'name': 'Jhon', 'language': 'c'})
	user.insert({'name': 'Anthony', 'language': 'python'})
	user.insert({'name': 'Jhon', 'language': 'c'})
	user.insert({'name': 'Anthony', 'language': 'python'})
	user.insert({'name': 'Jhon', 'language': 'c'})
	user.insert({'name': 'Anthony', 'language': 'python'})
	user.insert({'name': 'Jhon', 'language': 'c'})
	user.insert({'name': 'Anthony', 'language': 'python'})
	user.insert({'name': 'Jhon', 'language': 'c'})
	user.insert({'name': 'Anthony', 'language': 'python'})
	user.insert({'name': 'Jhon', 'language': 'c'})
	user.insert({'name': 'Anthony', 'language': 'python'})
	user.insert({'name': 'Jhon', 'language': 'c'})
	user.insert({'name': 'Anthony', 'language': 'python'})
	user.insert({'name': 'Jhon', 'language': 'c'})
	user.insert({'name': 'Anthony', 'language': 'python'})
	user.insert({'name': 'Jhon', 'language': 'c'})
	user.insert({'name': 'Anthony', 'language': 'python'})
	user.insert({'name': 'Jhon', 'language': 'c'})
	return 'Added User'

@app.route('/find')
def find():
	user = mongo.db.users
	cedric = user.find_one({'name':'Jhon'})
	return 'You found ' + cedric['name'] + '. Lenguaje ' + cedric['language']

@app.route('/update')
def update():
	user = mongo.db.users
	jhon = user.find_one({'name': 'Jhon'})
	jhon['language'] = 'javascript'
	user.save(jhon)
	return 'Actualizado'

@app.route('/delete')
def delete():
	user = mongo.db.users
	jhon = user.find_one({'name': 'Jhon'})
	user.remove(jhon)
	return 'Borrado'

if __name__ == '__main__':
	app.run(debug=True)