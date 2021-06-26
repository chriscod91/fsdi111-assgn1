#!/usr/bin/env python3
# coding: utf8
"""simple flask app"""

from flask import Flask #from flask package 
                        #import flask app

app = Flask(__name__)   #instantiate flask into the "app" variable

from app import routes
