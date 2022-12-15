#!/usr/bin/env python3
"""
This module handles the API for Joy of Painting
uses Flask and SQLAlchemy
"""

from flask import Flask, jsonify, request, abort, make_response
from api.v1.views import app_views
from flask_sqlalchemy import SQLAlchemy
import sqlite3
from flask_cors import CORS
import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + '/tmp/Joy_of_Painting.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
cors = CORS(app)
host = '0.0.0.0'
port = 5000
conn = sqlite3.connect('Joy_of_Painting.db')

def get_connection():
    conn = sqlite3.connect('Joy_of_Painting.db')
    return conn

@app_views.route('/paintings', methods=['GET'])
def get_paintings():
    #create a variable called month that is equal to the OS's current month
    month = os.getenv('MONTH')
    #create a sqlite3 query that aired during the current month
    query = "SELECT * FROM paintings WHERE month =?"
    #execute the query
    cursor = conn.cursor()
    cursor.execute(query, (month,))
    paintings = cursor.fetchall()
    return jsonify(paintings)
    


@app.run(host=host, port=port)
def run_server():
    """
    Run the Flask server.
    """
    app.run(host=host, port=port)