from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/", methods=['post', 'get'])
def index():
    return render_template('form.html')

@app.route("/signup_complete", methods=['post'])
def signup_complete():
    username = request.form['username']
    return render_template('welcome_page.html', name=username)

app.run()
