from flask import Flask, request, render_template, redirect
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


# validate user name
def validate_user(username):
    username_error = ""
    if len(username) < 3 or len(username) > 20 or username =="" or  " " in username:
        username_error = "Please enter a valid username that is between 3 and 20 characters in length with no spaces"
    return username_error

# validate  password
def validate_password(password):
    password_error = ""
    if password == "" or len(password) < 3 or len(password) > 20 or " " in password:
            password_error = "please enter a valid password between 3 to 20 characvters in length with no spaces"
    return password_error

# validate password verify input
def validate_verifypass(password, verifypass):
    verifypass_error = ""
    if verifypass != password:
        verifypass_error = "Your password fields do not match, please re-enter"
    return verifypass_error


#validate user email
def validate_email(email):
    email_error = ""
# if email contains more than one @ and more than one . , return error message
    if len(email) < 3 or len(email) > 20 or " " in email:
        email_error = "please enter a valid email address"
    return email_error
  
    at_symbol = "@"
    at_symbol_count = email.count(at_symbol)
   
    if at_symbol_count != 1:
        email_error = "please enter a valid email address"
        return email_error

    period = "."
    period_count = email.count(period)
   
    if period_count != 1:
        email_error = "please enter a valid email address"
        return email_error


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def validate():

    username = request.form["username"]
    password = request.form["password"]
    verifypass = request.form["verifypass"]
    email = request.form["email"]
    
    user_error = validate_user(username)
    pass_error = validate_password(password)
    verify_error = validate_verifypass(password, verifypass)

    email_error_error = ""
    if email != "":
        email_error_error = validate_email(email)

    if user_error or pass_error or verify_error or email_error_error:
        return render_template('index.html', user_error_placeholder=user_error, password_error_placeholder=pass_error, verifypass_error_placeholder=verify_error, email_error_placeholder=email_error_error, username=username, email=email )
 
 # if there are no errors, return the welcome message
    else:
        return render_template('welcome_page.html', name=username)

app.run()
