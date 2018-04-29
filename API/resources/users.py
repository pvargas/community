import json

from flask import Blueprint, jsonify, g
from flask_restful import Api, Resource, marshal, marshal_with, request, abort
from flask_marshmallow import Marshmallow
from playhouse.shortcuts import dict_to_model, model_to_dict
from webargs import fields
from webargs.flaskparser import use_args

import models

from auth import auth

users_api = Blueprint('resources.users', __name__)
api = Api(users_api)


class UserList(Resource):
    def get(self):
        try:
            query = models.User.select().order_by(models.User.id)
            user_schema = models.UserSchema(many=True, only=('name','id','member_since', 'is_moderator'))
            output = user_schema.dump(query).data
            return jsonify({'users': output})
        except:
            abort(500, message="Oh, no! The Community is in turmoil!")

    def post(self):
        if(request.is_json):          
            data = request.get_json(force=True)
            if 'name'in data:
                name = data['name']
                email = data['email']
                password = data['password']

                                
                query = models.User.select().where((models.User.name == name) | (models.User.email == email))
                
                if query.exists():
                    abort(422, message='Username or email already exist.')

                else:                   
                    user = models.User.create_user(name, email, password)

                    query = models.User.get(models.User.id == user.id)
                    user_schema = models.UserSchema(only=('name','id','member_since', 'is_moderator'))
                    output = user_schema.dump(query).data
                    return jsonify({'user': output})
                

                return jsonify(user)
            else:
                return jsonify({"error":{'message':'No username provided.'}})
        else:
            abort(400, message="Not JSON data.")

class User(Resource):
    def get(self, name):

        try:            
            query = models.User.get(models.User.name == name)

            user_schema = models.UserSchema(only=('name','id','member_since', 'is_moderator'))
            output = user_schema.dump(query).data
            return jsonify({'user': output})
            
        except :
            abort(404, message="Record does not exist.")

api.add_resource(UserList, '/users', endpoint='users')
api.add_resource(User, '/users/<name>', endpoint='user')
