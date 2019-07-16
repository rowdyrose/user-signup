from flask import Flask, request, render_template, redirect
import cgi
import os
from functions import *

app = Flask(__name__)
app.config['DEBUG'] = True

# validate user name
def validate_user(username):
    
    if len(username) <=4 or len(username) > 12 or username =="":   
        username_error = "Please enter a valid username that is between 4 and 12 characters in length"
        return False
    elif " " in username:
        username_error = "Please enter a user name with out spaces"
        return False

#validate  password
def password(password):
    password_error = "please enter a valid password"
    if password == "" or password <= 3 or password > 12:
        return password_error
# validate password verify input

def validate_verifypass(verifypass):
    verifypass_error = "Your password fields do not match, please re-enter"
    if verifypass != password:
        return verifypass_error

#validate user email
    #only validating if something is entered in this field
   # if email != "":



# if there are no errors, return the welcome message

@app.route("/", methods=['post', 'get'])
def index():
    return render_template('form.html')


@app.route("/signup_complete", methods=['post'])
def signup_complete():
    username = request.form['username']
    password()
    return render_template('welcome_page.html', name=username)

app.run()
