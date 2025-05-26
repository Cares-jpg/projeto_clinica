from flask import Flask

app = Flask(__name__)

from clinica.views import loginPage,homePage