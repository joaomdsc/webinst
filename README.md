# webinst

`webinst` (as in "web application instance") is a script to instantiate a web
application skeleton. The default skeleton follows Miguel Grinberg's Flask
mega-tutorial, an alternate skeleton includes the connexion module to provide a
swagger description of a REST API.

Running the `webinst` script creates a sub-directory for the application in the
current directory, and installs every dependency (currently flask and
flask-wtf, and optioinnaly connexion[swagger-ui]) so that the application can
be immediately run.

## Usage

Run the script with the following command :

``` console
py webinst.py <dst_path> <app_name> [rest]
```

where `dst_path` is the directory where the application code will be found,
`app_name` is the application name, and `rest` is an optional parameter
indicating whether the application will expose a REST API defined in a
swagger.yml file, as per the `connexion` module.

Running this script will create an `app_name` sub-directory under `dst_path`
(creating the `dst_path` directory itself, if it does not exist) : `cd` into
it, and activate the virtual environment.

If the `rest` parameter was specified, you'll need the following command to run
the app:

``` console
py app.py
```

Otherwise (there's a python package in this case), the app is run by calling:

``` console
flask run
```

In both cases, the application front-end can be found at `localhost:5000`.
