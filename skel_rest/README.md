# Contents

This directory includes code for a flask/connexion-based web server, exposing a
REST API.

# App structure

We're following this [tutorial](https://realpython.com/flask-connexion-rest-api/)
from RealPython. Note that this does not create a package for the flask server,
as Miguel Grinberg does.

The `app.py` file is the main module. We use
the [connexion](https://github.com/spec-first/connexion) module, so Flask is
not called directly, instead we create a `connexion.App` module:

``` python
# Internally, the Flask app is still created
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')
```

The module also includes code to run the server:

``` python
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
```

# Usage

Change to the `invivoo/rest` directory, activate the virtual environment, and
run the following command:

```
py app.py
```

The server is listening on the default 5000 port. The home page at
localhost:5000 displays some boilerplate message, the api is found under
localhost:5000/api (as defined in `swagger.yml`), and the swagger descriptions
are in localhost:5000/api/ui.


