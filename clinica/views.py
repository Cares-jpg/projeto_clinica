from clinica import app
from flask import render_template,url_for

@app.route('/')
def loginPage():
    return render_template('login.html')

@app.route('/home')
def homePage():
    return render_template('home.html')