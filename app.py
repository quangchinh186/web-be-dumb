import os
from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
from SQLAlchemyEngine import SQLAlchemyEngine
from resources import blueprints

#flask app
app = Flask(__name__)
#setup cors
CORS(app, resources={r"/*":{"origins":"*"}})
#setup socket io

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return "Hello World"

#register blueprints
for bp in blueprints:
    app.register_blueprint(bp)

