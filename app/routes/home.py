from flask import Blueprint, render_template

views_home = Blueprint('views_home',__name__)

def render_home_template():
    return render_template("home.html")

@views_home.route("/")
def home():
    return render_home_template()