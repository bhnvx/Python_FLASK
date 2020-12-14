from flask import Blueprint, request, url_for, render_template, flash, redirect
from flask import current_app as app

main = Blueprint('main', __name__, url_prefix='/')

@main.route('/', methods=['GET'])
def index():
    return render_template('/main/index.html')