from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/processlogin', methods = ['POST'])
def process_login():

    uname = request.form['username']
    pword = request.form['pwd']

    #Connect to database then SELECT * FROM users WHERE username = uname AND password = pword

    return uname + " " + pword

@app.route('/signup/', methods=['GET', 'POST'])
def signup():
    if(request.method == 'POST'):
        fname = request.form['firstname']
        lname = request.form['lastname']

        redirect(url_for('/success'))
    else:
        return render_template("signup.html")

@app.route('/home/')
def home():
    return render_template("home.html")

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)
