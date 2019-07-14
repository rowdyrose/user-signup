from flask import Flask, request, render_template
import os
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('form.html')
def empty_value(val):
    if val:
        return True
    else:
        return False

def char_length(val):
    if len(val) > 4 and len(val) < 20:
        return True
    else:
        return False

def email_symbol(val):
    if val.count('@') <= 1 and x.count('.') >= 1:
        return True
    else:
        return False



@app.route("/signup_complete", methods=['post'])
def signup_complete():
    username = request.form['username']
    return render_template('welcome_page.html', name=username)

app.run()
