
# installing flask app
# pip3 install Flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/fauzia')
def hello_fauzia():
    return 'Hello Fauzia!'

@app.route('/HHA504')
def hello_HHA504():
    return 'Hello HHA504'

if __name__ == '__main__':
    app.run(debug=True, host='localhost' , port=80)

