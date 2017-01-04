import flask

from .foo import foo
from .bar import bar

app = flask.Flask(__name__)

@app.route('/foo')
def get_foo():
    return foo()

@app.route('/bar')
def get_bar():
    return bar()
