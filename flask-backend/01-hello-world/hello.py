from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello, World!</h1>"

@app.route('/cards/')
def user():
    d = {"something":useful}
    return jsonify(d)   

@app.route('/profile/')
def profile():
    return "success"

if __name__ == '__main__':
    app.run(debug=True)

