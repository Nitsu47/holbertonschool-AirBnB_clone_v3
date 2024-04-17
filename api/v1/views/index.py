#!/usr/bin/python3
""" Index module """
from api.v1.views import app_views
from flask import Flask


@app_views.route("/status", app_views)
def json_str():
    """Returns a JSON str"""
    return ("status": "OK")
