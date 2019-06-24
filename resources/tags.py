import models

import json

from flask import Blueprint, jsonify, abort
from flask_restful import Api, Resource, marshal, marshal_with, request
from flask_marshmallow import Marshmallow
from playhouse.shortcuts import dict_to_model, model_to_dict
from webargs import fields
from webargs.flaskparser import use_args

tags_api = Blueprint('resources.tags', __name__)
api = Api(tags_api)


class TagList(Resource):
    def get(self):
        try:
            query = models.Tag.select().order_by(models.Tag.id)
            tag_schema = models.TagSchema(many=True)
            output = tag_schema.dump(query).data

            models.DATABASE.close()

            return jsonify({'tags': output})
        except:
            models.DATABASE.close()
            #pass

    def post(self):
        try:
            if(request.is_json):
                data = request.get_json(force=True)
                if 'name' in data:

                    name = data['name']

                    query = models.Tag.select().where(models.Tag.name == name)
                    if query.exists():
                        return jsonify({'error': {'message': 'duplicate tag.'}})
                    else:
                        tag_id = models.Tag.insert(name=name).execute()
                        query = models.Tag.get(models.Tag.id == tag_id)
                        tag_schema = models.UserSchema()
                        output = tag_schema.dump(query).data

                        models.DATABASE.close()

                        return jsonify({'tag': output})
                else:
                    models.DATABASE.close()
                    return jsonify({'error': {'message': 'missing required field(s).'}})
            else:
                models.DATABASE.close()
                abort(400)
        except:
            models.DATABASE.close()
            #pass


class Tag(Resource):
    def get(self, name):
        try:
            query = models.Tag.get(models.Tag.name == name)
            tag_schema = models.TagSchema()
            output = tag_schema.dump(query).data

            models.DATABASE.close()

            return jsonify({'tag': output})

        except models.DoesNotExist:
            models.DATABASE.close()
            return jsonify({'error': {'message': 'record does not exist.'}})


api.add_resource(TagList, '/tags', endpoint='tags')
api.add_resource(Tag, '/tags/<name>', endpoint='tag')
