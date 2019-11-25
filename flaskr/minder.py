import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
import requests

bp = Blueprint('minder', __name__, url_prefix='/minder')

@bp.route("/modal")
def modal():
    return render_template("modal.html")

@bp.route("/yes")
def yes():
    r = requests.get("https://api.flock.co/v1/chat.sendMessage?to=u:olhoyhclihiyyhhy&text=" + "Awesome Akshay" + "&token=b9c7b452-1145-4797-87cb-c92991fb6732")
    return "awesome"

@bp.route("/no")
def no():
    r = requests.get("https://api.flock.co/v1/chat.sendMessage?to=u:olhoyhclihiyyhhy&text=" + "Awesome Harsh" + "&token=b9c7b452-1145-4797-87cb-c92991fb6732")
    return "awesome"
