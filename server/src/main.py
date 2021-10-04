from flask import Flask
from flask_cors import CORS
from flask import request, jsonify
from flask import render_template
import json

import os
import sys

sys.path.append(os.getcwd())

def make_app():
    app = Flask(__name__)
    CORS(app)


    return app
