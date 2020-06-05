from flask import Flask, jsonify, request, redirect, url_for, render_template
from flask_pymongo import PyMongo
from pymongo import MongoClient

#framework init
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'colegio'

#change colegio to your database name
app.config['MONGO_URI'] = 'mongodb://mongodb:27017/colegio'


mongo = PyMongo(app)

#Method to get elements from the collection
@app.route('/framework', methods=['GET'])
def get_all_students():
    alumnos = mongo.db.alumnos
    output = []
    for query in alumnos.find():
        output.append({'_id': query['_id'], 'nombre': query['nombre'], 'edad': query['edad']})
    return jsonify({'result': output})



#Method to add students.
@app.route('/framework', methods=['POST'])
def add_student():
    
    alumnos = mongo.db.alumnos

    _id = request.json['_id']
    nombre = request.json['nombre']
    edad = request.json['edad']

    #add student to collection
    newstudent = alumnos.insert({'_id': _id, 'nombre': nombre, 'edad': edad})
    getnewstudent = alumnos.find_one({'_id': newstudent})

    #returns a query on success
    output = {'_id': getnewstudent['_id'], 'nombre': getnewstudent['edad'], 'edad': getnewstudent['edad']}
    return jsonify(output)


#Method to delete estudiant.
@app.route('/framework/<_id>',methods=['DELETE'])
def delete_student(_id):
    alumnos = mongo.db.alumnos
    
    alumnos.delete_one({'_id': _id})
    
    output = {'message': _id + ' Has been deleted'}
    return jsonify(output)


#Method to modify student
@app.route('/framework',methods=['PUT'])
def update_student():
    alumnos = mongo.db.alumnos
    _id = request.json['_id']
    nombre = request.json['nombre']
    edad = request.json['edad']
    alumnos.update_many({'_id': _id}, {'$set': {
        'nombre': nombre,
        'edad': edad
    }})
    output = {'message': 'Updated'}
    return jsonify(output)

#exec app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)