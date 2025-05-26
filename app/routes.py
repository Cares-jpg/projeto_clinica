from flask import Flask, render_template, url_for
from models.database import db, Paciente
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clinica.db'

db.init_app(app)

@app.route('/')
def loginPage():
    return render_template('login.html')

@app.route('/home')
def homePage():
    return render_template('home.html')

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run()