#!/usr/bin/python3
""" This module will start the flask web application
"""
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def tear_apps(error):
    """This will tear down any data"""
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def list_all__state(id=None):
    """render templates and jinja implementation"""
    from models.state import State

    found = False
    sList = storage.all(State).values()
    if id:
        for value in sList:
            if value.id == id:
                sList = value
                found = True
    return render_template('9-states.html', sList=sList,
                           found=found, mid=id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
