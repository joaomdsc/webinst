# webinst

`webinst` (as in "web application instance") is a script to instantiate a web
application skeleton. The skeleton follows Miguel Grinberg's Flask
mega-tutorial.

Running the `webinst` script creates a sub-directory for the application in the
current directory, and installs every dependency (currently flask and
flask-wtf) so that the application can be immediately run.

## Usage

Run the script with the following command :

``` console
py webinst.py <dst_path> <app_name> [rest]
```

where `dst_path` is the directory where the application code will be found,
`app_name` is the application name, and `rest` is an optional parameter
indicating where the application will expose a REST API.

Running this script will create an `app_name` sub-directory under `dst_path`
(creating the `dst_path` directory itself, if it does not exist) : `cd` into
it, activate the virtual environment, and you can run `flask run`. The
application front-end can be found at `localhost:5000`.
