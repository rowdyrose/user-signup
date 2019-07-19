from flask import Flask, request, render_template, redirect
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True



# validate user name
def validate_user(username):
    if len(username) < 3 or len(username) > 20 or username =="":   
        username_error = "Please enter a valid username that is between 4 and 12 characters in length"
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
    else
        return 



#validate user email
    #only validating if something is entered in this field
def validate_email
        if email != "":
                #return True
       #  elif email == 



# if there are no errors, return the welcome message

@app.route("/", methods=['POSTef index():
    return render_template('form.html')


@app.route("/signup_complete", methods=['post'])
def signup_complete():

    return render_template('welcome_page.html', name=username)

app.run()
