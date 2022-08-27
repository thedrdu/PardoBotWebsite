from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def home():
    return render_template("index.html", title="Home")

@app.route('/features')
def help():
    return render_template("features.html", title="Features")
