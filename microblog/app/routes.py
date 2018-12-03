from app import app #first app- is an packat, second app- is the varible defiined other package

@app.route('/')
@app.route('/index')

def index():
    return 'Hello, World!'
