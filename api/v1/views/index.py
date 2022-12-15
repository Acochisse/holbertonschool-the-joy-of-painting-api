#!/usr/bin/env python3
"""
this module handles the index for web views in the api
"""

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
from api.v1.views import app_views
import sqlite3
import os
import sys

app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def index():
    """
    This function returns the index.html page
    """
    return render_template('index.html')


@app.route('/painting_of_the_month/', methods=['GET'], strict_slashes=False)
def painting_of_the_month():
    """this function queries the database through sqlite3 to return a list of all paintings that aired during the current month"
    """
    conn = sqlite3.connect('Joy_of_Painting.db')
    c = conn.cursor()
    c.execute("SELECT * FROM paintings WHERE month = 'January'")
    paintings = c.fetchall()
    return render_template('painting_of_the_month.html', paintings=paintings)