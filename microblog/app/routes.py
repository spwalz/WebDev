from app import app #first app- is an packat, second app- is the varible defiined other package

@app.route('/')
@app.route('/index')

def index():
    user= {'username': 'Sarah'}
    #return 'Hello, ' + user['username']
    return  render_template('index.html', title='Home', user=user)

