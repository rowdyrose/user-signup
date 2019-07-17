from flask import Flask, request, render_template, redirect
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

# validate user name
def validate_user(username):
    username = ["username"]
    if len(username) <= 4 or len(username) > 12 or username =="":   
        username_error = "Please enter a valid username that is between 4 and 12 characters in length"
        return username_error
    elif " " in username:
        username_error = "Please enter a user name with out spaces"
        return username_error

#validate  password
def validate_password(password):
    password = ["password"]
    password_error = "please enter a valid password between 4 to 12 characvters in length"
    if password == "" or len(password) <= 3 or len(password) > 12:
        return password_error
# validate password verify input

def validate_verifypass(verifypass):
    verifypass = ["verifypass"]
    password = ["password"]
    verifypass_error = "Your password fields do not match, please re-enter"
    if verifypass != password:
        return verifypass_error

#validate user email
    #only validating if something is entered in this field
#def val
        #email = ["email"]
        #if email != "":
                #return True
       #  elif email == 



# if there are no errors, return the welcome message

@app.route("/", methods=['get'])
def index():
    return render_template('form.html')


@app.route("/signup_complete", methods=['post'])
def signup_complete():
    
    username = request.form['username']
    password = request.form[ 'password']
    verifypass = request.form['verifypass']
    #email = request.form['email']
    
    validate_user(username)
    validate_password(password)
    validate_verifypass(verifypass)
    return render_template('welcome_page.html', name=username)

app.run()
