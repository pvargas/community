import json

from flask import Blueprint, jsonify, g, Response
from flask_restful import Api, Resource, request, abort
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields 
from playhouse.shortcuts import dict_to_model, model_to_dict
from webargs import fields
from webargs.flaskparser import use_args

from peewee import JOIN, fn

import models

from auth import auth

import validators


posts_api = Blueprint('resources.posts', __name__)
api = Api(posts_api)

def is_valid(data):
    # validates new user data
    if ('title' in data and 'content' in data and
        'is_url' in data and 'author' in data and
        'tags' in data):

        if (not data['title'] or not data['content'] or not data['author'].isalnum() or
            len(data['title']) > 300):
            return False

        if data['is_url']:
            if not validators.url(data['content'].strip()):
                return False
        
        return True
        
    else: 
        return False

def insert_tags(tags, post_id):
    print()
    for i in tags:
        print(i["name"])
        if not models.Tag.select().where(models.Tag.name == i["name"].lower()).exists():
            print("insert^tags log 1")
            tag = models.Tag.create_tag(i["name"].lower())
            print("insert^tags log 2")
            #models.PostTags.create_relationship(post_id, tag.id)
            models.PostTags.insert(post_id=post_id, tag_id=tag.id).execute()
        else:
            print("insert^tags log 3")
            tag = models.Tag.get(models.Tag.name == i["name"].lower())
            print("insert^tags log 4")
            print("tag^id =", tag.id)
            #models.PostTags.create_relationship(post_id, tag.id)
            models.PostTags.insert(post_id=post_id, tag_id=tag.id).execute()
            print("last log line")


class PostList(Resource):

    def get(self):
        try:
            query = models.Post.select().order_by(models.Post.id)
            post_schema = models.PostSchema(many=True, exclude=('author.password', 'author.email', 'author.is_moderator', 'author.member_since'))
            #only=('id', 'content', 'title', 'author.name', 'author.id', 'is_url', 'created_at', 'last_modified')
            output = post_schema.dump(query).data

            return jsonify({'posts': output})
        except:
            abort(500, message="Oh, no! The Community is in turmoil!")

    @auth.login_required
    def post(self):
        print('it got here 1')
        if(request.is_json):
            print('it got here 2')
            data = request.get_json(force=True)

            if is_valid(data):

                title = data['title'].strip()
                is_url = data['is_url']
                name = data['author'].strip()
                content = data['content'].strip()
                tags = data['tags']                       

                author = models.User.get(models.User.name == name)
                print(g.user)
                print(author)
                print(name)  
                
                if g.user != author:
                    print("user is different")
                    abort(401)

                print("user is NOT different")

                query = models.Post.select().where(models.Post.title == title, models.Post.content == content,
                                                   models.Post.author == author.id)

                if query.exists():
                    print('duplicate')
                    abort(400, message="Duplicate entry.")

                else:
                    print('log 2')
                    post_id = models.Post.insert(
                        title=title, is_url=is_url, author=author, content=content).execute()
                    print('log 3')
                    print("*post id =", post_id)
                    insert_tags(tags, post_id)
                    print('log 4')

                    postid = int(post_id)
                    query = models.Post.get(models.Post.id == postid)
                    post_schema = models.PostSchema(only=('id', 'content', 'title', 'author.name', 
                                                    'author.id', 'is_url', 'created_at', 
                                                    'last_modified'))

                    print('log 6')
                    output = post_schema.dump(query).data
                    print('log 7')
                    return jsonify({'post': output})
            else:
                abort(400, message="Missing or invalid fields.")
        else:
            abort(400, message='Not JSON data')


class Post(Resource):
    def get(self, id):
        try:
            
            query = models.Post.get(models.Post.id == id)
            post_schema = models.PostSchema(only=('id', 'content', 'title', 'author.name', 'author.id', 'is_url', 
            'created_at', 'last_modified'))
            
            output = post_schema.dump(query).data

            return jsonify({'post': output})

        except models.DoesNotExist:
            abort(404, message="Record does not exist.")

    #@auth.login_required
    def put(self, id):
        try:
            data = request.get_json(force=True)
            if ('title' in data and 'content' in data and
                    'is_url' in data and 'author' in data):

                title = data['title']
                content = data['content']

            query = models.Post.update(
                title=title, content=content).where(models.Post.id == id)
            query.execute()

            return Response(status=200, mimetype='application/json')

        except models.DoesNotExist:
            abort(404, message="Record does not exist.")

    @auth.login_required
    def delete(self, id):
        try:        
            post = models.Post.select().where(models.Post.id == id).get()
                
            if g.user != post.author:
                print("user is different")
                abort(401)

            models.PostVotes.delete().where(models.PostVotes.post == id).execute()            
            models.PostTags.delete().where(models.PostTags.post == id).execute()            
            models.Comment.delete().where(models.Comment.post == id).execute()            
            models.Post.delete().where(models.Post.id == id).execute()
            
        except:
            abort(500, message="Oh, no! The Community is in turmoil!")
        
        return Response(status=204, mimetype='application/json')

class PostTags(Resource):
    def get(self, id):

        try:
            query = (models.Tag.select(models.Tag).
                join(models.PostTags, JOIN.RIGHT_OUTER).where(models.PostTags.post == id))            
            
        except:            
            abort(404, message="Record does not exist.")
        
        tag_schema = models.TagSchema(many=True)
        output = tag_schema.dump(query).data
        return jsonify({'tags': output})
    
class PostComments(Resource):
    def get(self, id):

        try:
            query = (models.Comment.select(models.Comment).where(models.Comment.post == id))            
            
        except:            
            abort(404, message="Record does not exist.")
        
        comment_schema = models.CommentSchema(many=True, only=('id', 'content', 'author.id',
                                                'author.name', 'created_at', 'last_modified', 'parent_id'))
        output = comment_schema.dump(query).data
        return jsonify({'comments': output})

class PostVotes(Resource):
    def get(self, id):
        if(request.is_json):
            try:
                query = models.PostVotes.select().where(models.PostVotes.post_id == id)                
            except:            
                abort(404, message="Record does not exist.")
            
            try:

                schema = (models.PostVotesSchema(many=True, 
                    only=('post_id', 'value', 'voter.name', 'voter.id')))

                output = schema.dump(query).data
                
                summation = 0
                for i in output:
                    summation += i['value']

                return jsonify({'votes': output, 'total':summation})
            except: 
                abort(500, message="Oh, no! The Community is in turmoil!")
       
        else:
            abort(400, message='Not JSON data')

    @auth.login_required
    def post(self, id):
        if(request.is_json):
        
            data = request.get_json(force=True)
            try:
                print('log 1')
                value = data['value']
                voter = data['voter']
                user = models.User.get(models.User.name == voter)

                if not (value >= 0 and value <= 1):
                    abort(400, message="Missing or invalid fields.")

                print('log 2')
            except:
                print('log 3')
                abort(400, message="Missing or invalid fields.")

            print('log 4')
            
            if g.user != user:
                abort(401)
            
            query = models.PostVotes.select().where((models.PostVotes.voter == user.id) & (models.PostVotes.voter == user.id))
            print('log 5')

            if query.exists():
                models.PostVotes.update(value=value).where((models.PostVotes.voter == user.id) & (models.PostVotes.voter == user.id)).execute()
                print('update')
                Response(status=200, mimetype='application/json')
            
            else:
                models.PostVotes.insert(post=id, voter=user.id, value=value).execute()     
                print('new')
                Response(status=200, mimetype='application/json')


        else:
            abort(400, message='Not JSON data')

        return Response(status=200, mimetype='application/json')
        
api.add_resource(PostList, '/posts', endpoint='posts')
api.add_resource(Post, '/posts/<int:id>', endpoint='post')
api.add_resource(PostTags, '/posts/<int:id>/tags', endpoint='post_tags')
api.add_resource(PostComments, '/posts/<int:id>/comments', endpoint='post_comments')
api.add_resource(PostVotes, '/posts/<int:id>/votes', endpoint='post_votes')
