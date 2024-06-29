from flask import Flask
from markupsafe import escape

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    @app.route("/<name>")
    def hello_someone(name):
        return f"Hello, {escape(name)}!"

    return app

app = create_app({"TESTING": False})
