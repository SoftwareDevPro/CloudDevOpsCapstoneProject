
from flask import Flask

app = Flask(__name__)

# Testing locally via run_docker.sh
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/hi
# http://127.0.0.1:8000/hello
# http://127.0.0.1:8000/greet
# http://127.0.0.1:8000/greet/Chris%20Adamson

@app.route('/')
@app.route('/hi')
@app.route('/hello')
def index():
    return '<h3>Hello, My name is Christopher Adamson</h3>'

@app.route('/greet', defaults={'name': 'Christopher Adamson'})
@app.route('/greet/<name>')
def greet(name):
    return '<h3>Hello, %s!</h3>' % name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
