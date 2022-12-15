#!/usr/bin/env python3
"""
This module handles the API for Joy of Painting
uses Flask and SQLAlchemy
"""

from flask import Flask, jsonify, render_template, request, abort, make_response
from api.v1.views import app_views
import sqlite3
from flask_cors import CORS
import json
import os

app = Flask(__name__)
cors = CORS(app)
host = '0.0.0.0'
port = 5000
conn = sqlite3.connect('Joy_of_Painting.db')

def get_connection():
    conn = sqlite3.connect('Joy_of_Painting.db')
    return conn

@app.route('/', methods=['GET'])
def index():
    return (render_template('login.html'), 200, {'Content-Type': 'text/html'})


@app.run(host=host, port=port)
def run_server():
    """
    Run the Flask server.
    """
    app.run(host=host, port=port)