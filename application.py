from flask import Flask, render_template
from bs4 import BeautifulSoup

import urllib.request

app = Flask(__name__)

@app.route('/')
def index():
    webpage = get_webpage()
    web_element = get_web_element(webpage)
    data = create_data(web_element)
    return str(data)

def get_webpage():    
    url = create_url('ArranN94')
    request = urllib.request.Request(url,  headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(request)
    return response.read()

def create_url(user):
    statSite = 'http://r6.tracker.network/profile/xbox/'
    return statSite + user

def get_web_element(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.select('.r6-season-rank__image:first-of-type')[0]

def create_data(web_element):
    user_data = {
        'rank': web_element.get('title'),
        'image_src': web_element.get('src')
    }
    return user_data

    