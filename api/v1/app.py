#!/usr/bin/python3
""" App module """
from models import storage
from api.v1.views import app_views
from flask import Flask
import os


app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """Teardown method to manage app context"""
    storage.close()


app.register_blueprint(app_views, url_prefix="api/v1")


if __name__ == "__main__":
    host = os.environ.get("HBNB_API_HOST", "0.0.0.0")
    port = int(os.environ.get("HBNB_API_PORT", "5000"))
    app.run(host=host, port=port, threaded=True)