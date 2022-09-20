import os
from flask import Flask
from flask import render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html", title="Home")

@app.route('/features')
def help():
    return render_template("features.html", title="Features")

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico')

# @app.route('/favicon.ico')
# def favicon():
#     app.send_static_file('favicon.ico')