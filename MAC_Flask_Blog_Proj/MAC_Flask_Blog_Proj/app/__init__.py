from flask import Flask
from app.main.index import main as main

app = Flask(__name__)

app.register_blueprint(main)