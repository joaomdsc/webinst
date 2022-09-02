# app/__init__.py: Flask application instance 

from flask import Flask

# This is the 'app' variable, a member of the 'app' package.
app = Flask(__name__)

# Below is the 'app' *package*, defined by the 'app' directory and this
# __init__.py script, as opposed to the 'app' variable defined above.
from app import routes
