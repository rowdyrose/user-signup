from flask import Flask, request, render_template, redirect, url_for
import cgi
import os
import re


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('form.html')

@app.route("/sign_up", methods=['POST'])
def sign_up():
    username = request.form["username"]
    password = ["password"]
    verify_password = ["verify_password"]
    email = ["email"]

    username_error = ""
    password_error = ""
    verify_password_error = ""
    email_error = ""

# validate user name
    if username =="":
        username_error = "Please enter a valid username"
    elif len(username) <=4 or len(username) > 14:
        username_error = "Please enter a username that is between 4 and 12 characters in length"
        username = ""
    elif " " in username:
        username_error = "Please enter a user name with out spaces"
        username = ""

#validate  password
    if verify_password =="" or verify_password != password:
        verify_password_error = "Your password fields do not macth, please re-enter"
        verify_password = ""

#validate user email
    #only validating if something is entered in this field
    if email != "":



# if there are no errors, return the welcome message
    if not username_error and not password_error and not verify_password_error and not email_error:
        username = username
        return render_template('welcome_page.html', username=username)
    else:
        return render_template('form.html', 
        username = username, 
        username_error = username_error, 
        password_error = password_error, 
        email = email, 
        email_error = email_error)

@app.route('/welcome_page')
def signup_complete():
    username = request.args.get('username')
    return render_template('welcome_page.html', username=username)

app.run()
