from flask import Flask, render_template

import stat_service

app = Flask(__name__)

@app.route('/')
def index():
    data = stat_service.get_data()
    return render_template('index.html', data=data)

   


    