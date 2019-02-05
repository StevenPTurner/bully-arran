from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return '<p>Index Page</p>'

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

@app.route('/user/<username>')
def show_user_profile(username):
    # Show the user profile for that user.
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # Show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # Show the subpath after /path/
    return 'Subpath %s' % subpath

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'POST LOGIN'
    else:
        return 'GET LOGIN'

@app.route('/user-url/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print (url_for('index'))
    print (url_for('login'))
    print (url_for('login', next='/'))
    print (url_for('profile', username='John Doe'))
