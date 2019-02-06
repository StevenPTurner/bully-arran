from flask import Flask, render_template

import stat_service

app = Flask(__name__)

@app.route('/')
@app.route('/<string:platform>/<string:username>')
def index(platform=stat_service.default_platform, username=stat_service.default_user):
    data = stat_service.get_data(platform, username)
    return render_template('index.html', data=data)

   


    