import json

from flask import Blueprint, jsonify, g, Response
from flask_restful import Api, Resource, marshal, marshal_with, request, abort
from flask_marshmallow import Marshmallow
from playhouse.shortcuts import dict_to_model, model_to_dict
from webargs import fields
from webargs.flaskparser import use_args

import models

from auth import auth

account_api = Blueprint('resources.account', __name__)
api = Api(account_api)

class Login(Resource):
    @auth.login_required
    def get(self):

        token = g.user.generate_auth_token()
        return jsonify({'token':token.decode('ascii'), 'name':g.user.name})

class Logout(Resource):
    @auth.login_required
    def get(self):

        token = request.headers['Authorization'][6:]
      
        g.user.expire_token()
        return Response('Logout successful', status=200)
        #jsonify({'response':response})

class Info(Resource):
    @auth.login_required
    def get(self):      
                
        query = models.User.get(models.User.name == g.user.name)

        user_schema = models.UserSchema(only=('name','id','member_since', 'is_moderator', 'email'))
        output = user_schema.dump(query).data
        return jsonify({'user': output})
            
        

        
api.add_resource(Login, '/account/login', endpoint='login')
api.add_resource(Logout, '/account/logout', endpoint='logout')
api.add_resource(Info, '/account/info', endpoint='info')