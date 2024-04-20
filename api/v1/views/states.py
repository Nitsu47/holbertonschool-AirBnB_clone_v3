#!/usr/bin/python3
"""Create a new view for State object"""


from flask import Flask, jsonify, request, abort
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def get_states():
    state = [state.to_dict() for state in storage.all(State).values()]
    return jsonify(state)


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def get_state_id(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=["DELETE"],
                 strict_slashes=False)
def delete_state(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route("/states", methods=["POST"], strict_slashes=False)
def add_state():
    state = request.get_json()
    if state is None:
        abort(400, "Not a JSON")
    if "name" not in state:
        abort(400, "Missing name")
    new = State(**state)
    new.save()
    return jsonify(new.to_dict()), 201


@app_views.route("/states/<state_id>", methods=["PUT"], strict_slashes=False)
def put_state(state_id):
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    data = request.get_json()
    if data is None:
        abort(400, "Not a JSON")
    for key, value in data.items():
        if key not in ["id", "created_at", "updated_at"]:
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200