from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('user_validation.html')


@app.route('/validate-user', methods=['POST'])
def validate_user():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if not username:
        username_error = 'That is not a valid username.'
        username = ''
        return render_template('user_validation.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=username, password=password, email=email)
    
    elif not password:
        password_error = 'That is not a valid password.'
        password = ''
        return render_template('user_validation.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=username, password=password, email=email)
	
    elif password != verify:
        verify_error = 'The passswords you entered do not match.'
        verify = ''
        return render_template('user_validation.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=username, password=password, email=email)
	
    elif not email:
        email_error = 'The email you entered is invalid.'
        email = ''
        return render_template('user_validation.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=username, password=password, email=email)

    else:
        return render_template('/validated_user.html')


if __name__ == '__main__':	
    app.run(debug=True)