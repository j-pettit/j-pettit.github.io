from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from datetime import datetime

blog = Flask(__name__)
blog.config['FLATPAGES_EXTENSION'] = '.md'

pages = FlatPages(blog)

@blog.route('/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)


def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    blog.run(debug=True)
