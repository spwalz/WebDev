from flask import render_template
from app import app
#first app- is an packat, second app- is the varible defiined other packag

@app.route('/')
@app.route('/index')

def index():
    user= {'username': 'Sarah'}
    #return 'Hello, ' + user['username']
    posts= [
        {
            'author': {'username':'John'},
            'body': 'Beutiful day in Portland!'
        },
        {
            'author':{'username': 'Susan'},
            'body':'The Avengers movies  are awesome!'
        }
        
        ]
        
    return  render_template('index.html', title= 'Home',  user=user, posts=posts)

