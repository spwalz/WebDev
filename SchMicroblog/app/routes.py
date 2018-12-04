#Payton Schubel
#12/3
#Ch. 1 "Hello World" routes.py

#import html template
from flask import render_template
#import app the application and app the variable
#(can use different names)
from app import app

#creates mapping between url and function
@app.route('/')
@app.route('/index') #can assign more than one url to same function
def index():
    #Fake user
    user = {'username':'Payton'}
    #fake list of posts
    posts = {
        {
            'author':{'username':'Aaina'}
            'body':'My name is Aaina, How\'s life?'
            }
        {
            'author':{'username':'Sarah'}
            'body':'How you doin\', Payton?'
            }
        }

    #could integrate html direct into app, but bad practice.
    #instead, html with enough variables to account for whatever is in
    #the html code
    return render_template('index.html', title = 'Home', user = user)
