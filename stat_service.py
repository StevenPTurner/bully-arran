from bs4 import BeautifulSoup
import urllib.request

default_platform = 'xbox'
default_user = 'ArranN94'
request_header = {
    'User-Agent': 'Mozilla/5.0'
    } 

def get_webpage():    
    url = create_url(default_platform, default_user)
    request = urllib.request.Request(url,  headers=request_header)
    response = urllib.request.urlopen(request)
    return response.read()

def create_url(platform, user):
    return 'http://r6.tracker.network/profile/{0}/{1}'.format(platform, user)


# def get_web_element(html):
#     soup = BeautifulSoup(html, 'html.parser')
#     return soup.select('.r6-season-rank__image:first-of-type')[0]

# def create_data(web_element):
#     user_data = {
#         'rank': web_element.get('title'),
#         'image_src': web_element.get('src')
#     }
#     return user_data

# def is_good(rank):
#     rank_dict = {
#         'unranked': -1,
#         'copper': 0,
#         'bronze': 1,
#         'silver': 2,
#         'gold': 3,
#         'platinum': 4,
#         'diamond': 5
#     }
#     rank_value = rank_dict[rank]

#     if rank_value > 2:
#         return True
#     else:
#         return False

def main():
    print(create_url(default_platform,default_user))

if __name__ == "__main__":
    main()