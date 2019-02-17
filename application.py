from flask import Flask, render_template

import stat_service

app = Flask(__name__)

@app.route('/')
def index():
    data = stat_service.get_home_data()
    return render_template('index.html', data=data)

@app.route('/stats')
def stats():
    data = stat_service.get_best_season_data()
    return render_template('stats.html', data=data)


    