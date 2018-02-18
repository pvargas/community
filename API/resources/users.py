import json

from flask import Blueprint, jsonify, abort
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
        try:
            query = models.User.select().order_by(models.User.id)
            user_schema = models.UserSchema(many=True)
            output = user_schema.dump(query).data
            return jsonify({'users': output})
        except:
            pass

    def post(self):        
        try:
            if(request.is_json):            
                data = request.get_json(force=True)
                if 'name'in data:
                    name = data['name']
                    email = data['email']
                    query = models.User.select().where(models.User.name == name)
                    if query.exists():
                        return jsonify({"error":{'message':'Username already exists'}})
                    else:
                        user_id = models.User.insert(name=name, email=email).execute()
                        query = models.User.get(models.User.id == user_id)
                        user_schema = models.UserSchema()
                        output = user_schema.dump(query).data
                        return jsonify({'user': output})
                else:
                    return jsonify({"error":{'message':'No username provided.'}})
            else:
                abort(400)
        except:
            pass

class User(Resource):
    def get(self, name):
        try:
            query = models.User.get(models.User.name == name)
            user_schema = models.UserSchema()
            output = user_schema.dump(query).data
            return jsonify({'user': output})
            
        except models.DoesNotExist:
            return jsonify({'error': {'message': 'record does not exist.'}})

api.add_resource(UserList, '/users', endpoint='users')
api.add_resource(User, '/users/<name>', endpoint='user')
