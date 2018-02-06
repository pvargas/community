from flask import jsonify, Blueprint
from flask_restful import Resource, Api
import models

class PostList(Resource):
    def get(self):
        return jsonify({'Posts': [{'id':12, 'title':'Amazon Hacked!'}]})

class Post(Resource):
    def get(self, id):
        return jsonify({'id':12, 'title':'Amazon Hacked!'})

    def put(self, id):
        return jsonify({'id':12, 'title':'Amazon Hacked!'})

    def delete(self, id):
        return jsonify({'id':12, 'title':'Amazon Hacked!'})

posts_api = Blueprint('resources.posts', __name__)
api = Api(posts_api)
api.add_resource(PostList,'/posts', endpoint ='posts')
api.add_resource(Post,'/posts/<int:id>', endpoint ='post')