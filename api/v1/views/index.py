#!/usr/bin/python3
""" Index module """
from api.v1.views import app_views
from flask import Flask, jsonify


@app_views.route("/status")
def json_str():
    """Returns status in a JSON dic"""
    return jsonify({"status": "OK"})
