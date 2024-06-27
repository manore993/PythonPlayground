from flask import Flask
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hello")
def method_x():
    return 'Hello, World'

@app.route("/<name>")
def hello_someone(name):
    return f"Hello, {escape(name)}!"