import os

from flask import Flask , request, url_for
app = Flask(__name__)

@app.route('/')
def show_url_for():
    # display the url for a function
    return url_for('show_user_profile', username='jorge')

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
    
@app.route('/login', methods=['GET'])
def login():
    if request.values:
        return "username is " + request.values['username']
    else:
        return '<form method="get" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'

if __name__ == '__main__':
    app.debug = True
    app.run(app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 5000))))