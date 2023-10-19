from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)

@app.route('/')
def hello_world():
	return "Hello World!"

@app.route('/<path:name>')
def hello_user(name):
	return f"Hello {name}!"

@app.route('/index.html')
def hello_html(name=None):
	return render_template('index.html', name=name)