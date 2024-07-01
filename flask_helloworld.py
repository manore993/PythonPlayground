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
        return f"{escape(request.form['username'])} with {escape(request.form['password'])}" 
    
    @app.route("/user/<name>")
    def hello_someone(name):
        return f"Hello, {escape(name)}!"

    @app.route("/login/", methods=['POST'])
    def login_verification_post():
        username = escape(request.form['username'])
        password = escape(request.form['password'])
        if (username == 'toto' and password == 'toto95'):
            return f"Hello {username}!"
        if (username == 'admin' and password == 'adminpw'):
            return f"Hello {username}! You are the admin acoount."
        if (username == 'admin' and password == 'adminpw2145') or (username == 'toto' and password == 'toto8256') :
            return f"Username and password do not match. Try again"
    
    return app

app = create_app({"TESTING": False})
