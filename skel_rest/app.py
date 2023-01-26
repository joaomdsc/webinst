# app.py

# Note that when importing connexion, we no longer import Flask
from flask import render_template
import connexion

# Internally, the Flask app is still created
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
