#!/usr/bin/python3
""" Index module """
from api.v1.views import app_views
from flask import Flask, jsonify
from models import storage
from models.state import State


@app_views.route("/status")
def json_str():
    """Returns status in a JSON dic"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    '''Endpoint that retrieves the number of each objects by type'''
    obj_dict = {
            "cities": storage.count("City"),
            "amenities": storage.count("Amenity"),
            "places": storage.count("Place"),
            "states": storage.count("State"),
            "reviews": storage.count("Review"),
            "users": storage.count("User")
            }
    return jsonify(obj_dict)
