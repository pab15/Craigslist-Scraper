from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password12345'

from app import routes
