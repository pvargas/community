import json

from flask import Blueprint, jsonify, g, Response
from flask_restful import Api, Resource, marshal, marshal_with, request, abort
from flask_marshmallow import Marshmallow
from playhouse.shortcuts import dict_to_model, model_to_dict
from webargs import fields
from webargs.flaskparser import use_args

import models

from auth import auth


posts_api = Blueprint('resources.posts', __name__)
api = Api(posts_api)


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
            post_schema = models.PostSchema(many=True)
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
            if ('title' in data and 'content' in data and
                    'is_url' in data and 'author' in data and 'tags' in data):

                title = data['title']
                is_url = data['is_url']
                name = data['author']
                content = data['content']
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
                    post_schema = models.PostSchema()

                    print('log 6')
                    output = post_schema.dump(query).data
                    print('log 7')
                    return jsonify({'post': output})
            else:
                return jsonify({'error': {'message': 'missing required field(s).'}})
        else:
            abort(400, message='Not JSON data')


class Post(Resource):
    def get(self, id):
        try:
            query = models.Post.get(models.Post.id == id)
            post_schema = models.PostSchema()
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

    #@auth.login_required
    def delete(self, id):
        query = models.Post.delete().where(models.Post.id == id)
        query.execute()

        return Response(status=204, mimetype='application/json')


api.add_resource(PostList, '/posts', endpoint='posts')
api.add_resource(Post, '/posts/<int:id>', endpoint='post')
