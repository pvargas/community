import models
from auth import auth

import json

from flask import Blueprint, jsonify, Response, g
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

    @auth.login_required
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

    @auth.login_required
    def put(self, id):
        if(request.is_json):

            data = request.get_json(force=True)

            try:        
                comment = models.Comment.select().where(models.Comment.id == id).get()
                
            except:
                abort(404, message="Comment doesn't exist")
                    
            if g.user != comment.author:
                abort(401)
            
            if ('content' in data):
                content = data['content'].strip()

                query = models.Comment.update(content=content).where(models.Comment.id == id)
                query.execute()

                query_2 = models.Comment.get(models.Comment.id == id)

                comment_schema = models.CommentSchema(only=('content','post_id',
                            'author.name', 'author.id', 'id',
                             'created_at', 'last_modified'))
            
                comment = comment_schema.dump(query_2).data

                return jsonify({'comment': comment})
            else:
                abort(400, message="Missing or invalid fields.")

        else:
            abort(400, message='Not JSON data')

    @auth.login_required
    def delete(self, id):
        try:        
            comment = models.Comment.select().where(models.Comment.id == id).get()
            
        except:
            abort(404, message="Comment doesn't exist")
                
        if g.user != comment.author:
            # unauthorized
            abort(401)

        try:
            content='[removed by user]'
            query = models.Comment.update(content=content).where(models.Comment.id == id)
            query.execute()

            query_2 = models.Comment.get(models.Comment.id == id)

            comment_schema = models.CommentSchema(only=('content','post_id',
                        'author.name', 'author.id', 'id',
                            'created_at', 'last_modified'))
        
            comment = comment_schema.dump(query_2).data

            return jsonify({'comment': comment})
        except:
            abort(500, message="Oh, no! The Community is in turmoil!")
        
        return Response(status=204, mimetype='application/json')

class CommentVotes(Resource):

    def get(self, id):
        
        try:
            
            query = models.CommentVotes.select().where(models.CommentVotes.comment_id == id)
        except:
            abort(404, message="Record does not exist.")

        try:
            
            schema = (models.CommentVotesSchema(many=True,
                    only=('comment_id', 'value', 'voter.name', 'voter.id')))

            output = schema.dump(query).data

            summation = 0
            for i in output:
                summation += i['value']

            return jsonify({'votes': output, 'total': summation})
        except:
            abort(500, message="Oh, no! The Community is in turmoil!")

        

    @auth.login_required
    def post(self, id):
        if(request.is_json):
        
            data = request.get_json(force=True)
            try:
                print('log 1')
                value = data['value']
                voter = data['voter']
                user = models.User.get(models.User.name == voter)

                if not (value >= -1 and value <= 1):
                    abort(400, message="Missing or invalid fields.")

                print('log 2')
            except:
                print('log 3')
                abort(400, message="Missing or invalid fields.")

            print('log 4')
            
            if g.user != user:
                abort(401)
            
            query = models.CommentVotes.select().where((models.CommentVotes.comment == id) & (models.CommentVotes.voter == user.id))
            print('log 5')

            if query.exists():
                models.CommentVotes.update(value=value).where((models.CommentVotes.comment == id) & (models.CommentVotes.voter == user.id)).execute()
                print('update')
                Response(status=200, mimetype='application/json')
            
            else:
                models.CommentVotes.insert(comment=id, voter=user.id, value=value).execute()     
                print('new')
                Response(status=200, mimetype='application/json')


        else:
            abort(400, message='Not JSON data')

        return Response(status=200, mimetype='application/json')


api.add_resource(CommentList, '/comments', endpoint='comments')
api.add_resource(Comment, '/comments/<int:id>', endpoint='comment')
api.add_resource(CommentVotes, '/comments/<int:id>/votes', endpoint='comment_votes')
