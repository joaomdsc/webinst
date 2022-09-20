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
py webinst.py <my_app>
```

replacing `my_app` by the name of your application. This will create a `my_app`
sub-directory: `cd` into it, activate the virtual environment, and you can run
`flask run`. The application front-end is at `localhost:5000`.


