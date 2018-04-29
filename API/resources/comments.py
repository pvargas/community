import models
from auth import auth

import json

from flask import Blueprint, jsonify, Response
from flask_restful import Api, Resource, marshal, marshal_with, request, abort
from flask_marshmallow import Marshmallow
from playhouse.shortcuts import dict_to_model, model_to_dict
from webargs import fields
from webargs.flaskparser import use_args

comments_api = Blueprint('resources.comments', __name__)
api = Api(comments_api)


class CommentList(Resource):
    def get(self):
        try:
            query = models.Comment.select().order_by(models.Comment.id)            
            #query = models.Comment.select().join(models.User)
            comment_schema = models.CommentSchema(many=True, only=('content', 'id', 'post_id', 'created_at',
            'last_modified', 'author.id','author.name', 'parent_id'))
            output = comment_schema.dump(query).data
            
            return jsonify({'comments': output})
        except:
            abort(500, message="Oh, no! The Community is in turmoil!")

    #@auth.login_required
    def post(self):       
        print('log 1')
        if(request.is_json):
            print('log 2')
            data = request.get_json(force=True)
            print('log 3')
            try:
                
                print('log 4')

                content = data['content']
                author = data['author']
                post_id = data['post_id']
                parent_id = data['parent_id']

                print('log 5')
                print('author:', author)

                user = models.User.select().where(models.User.name == author).get()

            except:
                abort(400, message='Missing or invalid fields')
            
            print('user who made comment: ', user.name)
            try:
                query = models.Comment.select().where(models.Comment.content == content,
                models.Comment.post_id == post_id, models.Comment.author == user.id)                    
            except:
                print('log 6.1')
                abort(409, message='Duplicate comment.')
            
            
            if query.exists():              
                abort(409, message='Duplicate comment.')
                          
            
            comment_id = models.Comment.insert(content=content, author=user.id, 
                post_id=post_id, parent_id=parent_id).execute()

            query = models.Comment.get(models.Comment.id == comment_id)

            comment_schema = models.CommentSchema(only=('content', 'id', 'post_id', 'created_at',
            'last_modified', 'author.id','author.name', 'parent_id'))

            output = comment_schema.dump(query).data

            return jsonify({'comment': output})          
        else:
            abort(400, message='Request is not JSON')
        


class Comment(Resource):
    def get(self, id):
        try:
            query = models.Comment.get(models.Comment.id == id)
            comment_schema = models.CommentSchema(only=('content', 'id', 'post_id', 'created_at',
            'last_modified', 'author.id','author.name', 'parent_id'))
            output = comment_schema.dump(query).data
            return jsonify({'comment': output})
        except models.DoesNotExist:
            abort(404, message='Comment does not exists.')


api.add_resource(CommentList, '/comments', endpoint='comments')
api.add_resource(Comment, '/comments/<int:id>', endpoint='comment')
