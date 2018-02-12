from flask import Flask, jsonify

import models
from config import App as config
from resources.posts import posts_api
from resources.users import users_api
from resources.tags import tags_api
from resources.comments import comments_api

app = Flask(__name__)
app.register_blueprint(users_api, url_prefix=config.URL_PREFIX)
app.register_blueprint(posts_api, url_prefix=config.URL_PREFIX)
app.register_blueprint(tags_api, url_prefix=config.URL_PREFIX)
app.register_blueprint(comments_api, url_prefix=config.URL_PREFIX)


@app.route('/')
def root():
    return jsonify({'message': 'Nothing to see here.'})  


if __name__ == '__main__':
    models.initialize()
    app.run(debug=config.DEBUG)
