from flask import Flask, render_template

import urllib.request
import stat_service

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

   


    