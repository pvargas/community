import time, datetime

from flask import Flask, jsonify, g

import models
from config import App as config
from resources.posts import posts_api
from resources.users import users_api
from resources.tags import tags_api
from resources.comments import comments_api


start_time = time.time()

app = Flask(__name__)
app.register_blueprint(users_api, url_prefix=config.URL_PREFIX)
app.register_blueprint(posts_api, url_prefix=config.URL_PREFIX)
app.register_blueprint(tags_api, url_prefix=config.URL_PREFIX)
app.register_blueprint(comments_api, url_prefix=config.URL_PREFIX)


def up_time(seconds):
    t = time.time() - seconds
    m, s = divmod(t, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)


@app.route('/api')
def info():
    return jsonify({'Community API':{'Version':config.API_VERSION,'Up Time': up_time(start_time)}})  
    
@app.route('/')
def root():
    return '️✌👌💩👌✌️'


if __name__ == '__main__':
    models.initialize()
    app.run(debug=config.DEBUG)
