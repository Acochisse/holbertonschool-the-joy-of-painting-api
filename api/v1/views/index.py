#!/usr/bin/env python3
"""
this module handles the index for web views in the api
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
from api.v1.views import app_views

app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)
cors = CORS(app)


@app.route('/')
def index():
    """
    This function returns the index.html page
    """
    return render_template('index.html')
