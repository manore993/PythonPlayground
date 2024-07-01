from flask import Flask, request
from markupsafe import escape

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    @app.route("/", methods=['GET'])
    def hello_world():
        return "<p>Hello, World!</p>"

    @app.route("/", methods=['POST'])
    def hello_world_post():
        # TODO Do some if condition based on request data
        # TODO escape
        return f"{request.form['username']} with {request.form['password']}" 
    
    @app.route("/user/<name>")
    def hello_someone(name):
        return f"Hello, {escape(name)}!"


    return app

app = create_app({"TESTING": False})
