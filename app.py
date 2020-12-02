from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from jinja2 import Template 
import json
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
    
if __name__ == '__main__':
    app.run(debug=True)