from flask import Flask, request, render_template, redirect
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


# validate user name
def validate_user(username):
    if len(username) < 3 or len(username) > 20 or username =="":   
        username_error = "Please enter a valid username that is between 3 and 20 characters in length"
        return username_error
    elif " " in username:
        username_error = "Please enter a user name with out spaces"
        return username_error

#validate  password

def validate_password(password):
    password_error = "please enter a valid password between 3 to 20 characvters in length"
    if password == "" or len(password) < 3 or len(password) > 20:
        return password_error
# validate password verify input

def validate_verifypass(password, verifypass):
    verifypass_error = "Your password fields do not match, please re-enter"
    if verifypass != password:
        return verifypass_error


#validate user email
  
def validate_email(email):
    email_error = "please enter a valid email address"
        # if email contains more than one @ and more than one . , return error message
    if email == " " or len(email) < 3 or len(email) > 20:
        return email_error
   
    at_symbol = "@"
    at_symbol_count = email.count(at_symbol)
    
    if at_symbol_count != 1:
        return email_error

    period = "."
    period_count = email.count(period)
    
    if period_count != 1:
        return email_error
                     




@app.route("/", methods=['GET'])
def index():
    return render_template('form.html')

@app.route("/", methods=['POST'])
def validate():

    username = request.form["username"]
    password = request.form["password"]
    verifypass = request.form["verifypass"]
    email = request.form["email"]
    
    if email != "":
            validate_email(email)
                
    return render_template('form.html')

# if there are no errors, return the welcome message

@app.route("/signup_complete", methods=['post'])
def signup_complete():

    return render_template('welcome_page.html', name=username)

app.run()
