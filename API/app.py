from flask import Flask

import models
from config import App as config
from resources.posts import posts_api
from resources.users import users_api

app = Flask(__name__)
app.register_blueprint(users_api, url_prefix=config.URL_PREFIX)
app.register_blueprint(posts_api, url_prefix=config.URL_PREFIX)


@app.route('/')
def hello_world():
    return 'Hello there, Chamchee!'


if __name__ == '__main__':
    models.initialize()
    app.run(debug=config.DEBUG)
