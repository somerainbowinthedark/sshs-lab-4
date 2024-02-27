from flask import Flask
from blueprint import damage
import random
# creates and defines an app using flask
def make_app():
    app = Flask(__name__)
    app.register_blueprint(damage)
    return app
# sets up the website
if __name__ == '__main__':
    app = make_app()
    app.run(host='localhost', port=8081, debug=True)