import datetime
import time

import flask_cors
from flask import Flask, Response, g, jsonify, request
from flask_limiter import Limiter
from flask_limiter.util import get_ipaddr
from flask_mail import Mail, Message

import models
from auth import auth
from config import App as config
from resources.account import account_api
from resources.comments import comments_api
from resources.posts import posts_api
from resources.tags import tags_api
from resources.users import users_api

start_time = time.time()

application = Flask(__name__)
flask_cors.CORS(application)
application.register_blueprint(users_api, url_prefix=config.URL_PREFIX)
application.register_blueprint(posts_api, url_prefix=config.URL_PREFIX)
application.register_blueprint(tags_api, url_prefix=config.URL_PREFIX)
application.register_blueprint(comments_api, url_prefix=config.URL_PREFIX)
application.register_blueprint(account_api, url_prefix=config.URL_PREFIX)

def up_time(seconds):
    t = time.time() - seconds
    m, s = divmod(t, 60)
    h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

# limiter = Limiter(application, global_limits=['7200/hour'], key_func=get_ipaddr)
# limiter.exempt(users)

@application.route('/', methods=['GET'])
def info():
    '''
    msg = Message('Someone visited the API root', sender=mailconf.EMAIL, recipients=['matomario8@gmail.com'])
    mail.send(msg)
    '''
    return jsonify({'Community API': {'Version': config.API_VERSION, 'Up Time': up_time(start_time), 'deployment': '11'}})


if __name__ == '__main__':
    models.initialize()
    application.run(debug=config.DEBUG)
