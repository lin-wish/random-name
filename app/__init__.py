from flask import Flask, render_template, send_from_directory
from flask import request, abort
from collections import namedtuple

from config import app_config


def create_app(config_name):
    """ App factory function. """
    import requests
   
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    # app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/randnames')
    def randnames():
        req_url = 'http://uinames.com/api/?ext'
        
        
        try:
            r = requests.get(req_url)
            profile = r.json()
        except:
            raise
       
        return render_template('index.html', profile=profile)
        

    return app