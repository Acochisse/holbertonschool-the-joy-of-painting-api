#!/usr/bin/env python3
"""
This module handles the API for Joy of Painting
uses Flask and SQLAlchemy
"""

from flask import Flask, jsonify, request, abort, make_response
from api.v1.views import app_views
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///' + '/tmp/Joy_of_Painting.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
cors = CORS(app)
host = '0.0.0.0'
port = 5000

@app_views.route('/api/v1/paintings', methods=['GET'])
def get_paintings():
    """returns a list of paintings from the Joy_of_Painting.db by selecting the column month and returning all that match the current month
    """
    month = request.args.get('month')
    paintings = Painting.query.filter_by(month=month).all()
    return jsonify([painting.to_json() for painting in paintings])


@app.run(host=host, port=port)
def run_server():
    """
    Run the Flask server.
    """
    app.run(host=host, port=port)