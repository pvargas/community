import models

import json

from flask import Blueprint, jsonify, abort
from flask_restful import Api, Resource, marshal, marshal_with, request
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
            comment_schema = models.CommentSchema(many=True)
            output = comment_schema.dump(query).data
            return jsonify({'comments': output})
        except:
            pass

    def post(self):
        try:
            if(request.is_json):
                data = request.get_json(force=True)
                if 'content' in data:

                    content = data['content']


                    #TODO
                    #check for same user_id+content+post_id

                    query = models.Comment.select().where(models.Comment.content == content)
                    if query.exists():
                        return jsonify({'error': {'message': 'duplicate comment.'}})
                    else:
                        comment_id = models.Comment.insert(content=content).execute()
                        query = models.Comment.get(
                            models.Comment.id == comment_id)
                        comment_schema = models.UserSchema()
                        output = comment_schema.dump(query).data
                        return jsonify({'comment': output})
                else:
                    return jsonify({'error': {'message': 'missing required field(s).'}})
            else:
                abort(400)
        except:
            pass


class Comment(Resource):
    def get(self, id):
        try:
            query = models.Comment.get(models.Comment.id == id)
            comment_schema = models.CommentSchema()
            output = comment_schema.dump(query).data
            return jsonify({'comment': output})
        except models.DoesNotExist:
            return jsonify({'error': {'message': 'record does not exist.'}})


api.add_resource(CommentList, '/comments', endpoint='comments')
api.add_resource(Comment, '/comments/<int:id>', endpoint='comment')
