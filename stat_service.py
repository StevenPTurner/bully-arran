from bs4 import BeautifulSoup
import urllib.request

default_platform = '    xbox'
default_user = 'ArranN94'
default_threshhold = 2
request_header = {'User-Agent': 'Mozilla/5.0'} 


def get_webpage(url, header):    
    request = urllib.request.Request(url,  headers=header)
    response = urllib.request.urlopen(request)
    return response.read()

def create_url(platform, user):
    return 'http://r6.tracker.network/profile/{0}/{1}'.format(platform, user)


def get_rank_from_page(web_page):
    soup = BeautifulSoup(web_page, 'html.parser')
    return soup.select('.r6-season-rank__image:first-of-type')[0]

def create_data(rank_element,user):
    full_rank = rank_element.get('title').lower()
    rank_name = 'not ranked yet'
    rank_level = ''
    message = 'No'

    if 'ranked' not in full_rank:       
        rank_name = full_rank.split()[0]
        rank_level = full_rank.split()[1]

    if(is_good(rank_name, default_threshhold)):
        message = 'Yes'

    user_data = {
        'rank_name': rank_name.capitalize(),
        'rank_level': rank_level.upper(),
        'image_src': rank_element.get('src'),
        'good_yet': message,
        'username' : user
    }
    return user_data

def is_good(rank_name, threshhold):
    rank_name = rank_name.replace(' ', '_')
    rank_dict = {
        'not_ranked_yet': -1,
        'copper': 0,
        'bronze': 1,
        'silver': 2,
        'gold': 3,
        'platinum': 4,
        'diamond': 5
    }
    rank_value = rank_dict[rank_name]

    if rank_value > 2:
        return True
    else:
        return False

def get_data(platform=default_platform, user=default_user):
    url = create_url(platform, user)
    web_page = get_webpage(url, request_header)
    rank_element = get_rank_from_page(web_page)
    data = create_data(rank_element, user)
    return data