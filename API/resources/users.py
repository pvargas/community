import json

from flask import Blueprint, jsonify
from flask_restful import Api, Resource, marshal, marshal_with, request
from flask_marshmallow import Marshmallow
from playhouse.shortcuts import dict_to_model, model_to_dict
from webargs import fields
from webargs.flaskparser import use_args

import models

users_api = Blueprint('resources.users', __name__)
api = Api(users_api)

class UserList(Resource):
    def get(self):
        query = models.User.select()
        user_schema = models.UserSchema(many=True)
        output = user_schema.dump(query).data
        return jsonify({'users': output})  
    
    def post(self):
        #request.
        #models.User.insert(name='Gengis').execute()
        print (request.is_json)
        content = request.get_json()
        print (content)
        return jsonify({'name': 'Picasso'})  


class User(Resource):    
    def get(self, name):    
        #query = models.User.get(id=id)
        query = models.User.get(models.User.name == name)
        user_schema = models.UserSchema()
        output = user_schema.dump(query).data
        return jsonify({'user': output})    
        
    def delete(self, name):
        return jsonify({'name': 'Picasso'})



api.add_resource(UserList, '/users', endpoint='users')
api.add_resource(User, '/users/<name>', endpoint='user')
#api.add_resource(User, '/users/<int:id>', endpoint='user')
