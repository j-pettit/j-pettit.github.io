from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from datetime import datetime

blog = Flask(__name__)

@blog.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    blog.run(debug=True)
