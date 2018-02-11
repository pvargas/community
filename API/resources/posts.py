import models

import json

from flask import Blueprint, jsonify, abort
from flask_restful import Api, Resource, marshal, marshal_with, request
from flask_marshmallow import Marshmallow
from playhouse.shortcuts import dict_to_model, model_to_dict
from webargs import fields
from webargs.flaskparser import use_args

posts_api = Blueprint('resources.posts', __name__)
api = Api(posts_api)


class PostList(Resource):
    def get(self):
        try:
            query = models.Post.select().order_by(models.Post.id)
            post_schema = models.PostSchema(many=True)
            output = post_schema.dump(query).data
            return jsonify({'posts': output})
        except:
            pass

    def post(self):
        try:
            if(request.is_json):
                data = request.get_json(force=True)
                if ('title' in data and 'content' in data and 
                    'is_url' in data and 'author' in data and 'tags' in data):
                   
                    title = data['title']
                    is_url = data['is_url']
                    author = data['author']
                    content = data['content']
                    tags = data['tags']

                    query = models.Post.select().where(models.Post.title == title, models.Post.content == content,
                                                       models.Post.author == author, models.Post.tags == tags)
                    if query.exists():
                        return jsonify({'error': {'message': 'Duplicate entry.'}})
                    else:
                        post_id = models.Post.insert(title=title, is_url=is_url, author=author, content=content, tags=tags).execute()
                        query = models.Post.get(models.Post.id == post_id)
                        post_schema = models.PostSchema()
                        output = post_schema.dump(query).data
                        return jsonify({'post': output})
                else:
                    return jsonify({'error': {'message': 'missing required field(s).'}})
            else:
                abort(400)
        except:
            pass


class Post(Resource):
    def get(self, id):
        try:
            query = models.Post.get(models.Post.id == id)
            post_schema = models.PostSchema()
            output = post_schema.dump(query).data
            return jsonify({'post': output})
        except models.DoesNotExist:
            return jsonify({'error': {'message': 'record does not exist.'}})


api.add_resource(PostList, '/posts', endpoint='posts')
api.add_resource(Post, '/posts/<int:id>', endpoint='post')
