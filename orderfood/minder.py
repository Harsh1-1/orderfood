import functools
from db import MySQL

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
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

@bp.route("/randomUser")
def random_image():
    mysql = MySQL()
    db_meta = mysql.load_db_meta_data()
    mydb = mysql.create_mysql_db_object(db_meta['host'],db_meta['username'], db_meta['password'], db_meta['port'], db_meta['db'])
    query = "SELECT * FROM user_details ORDER BY RAND() LIMIT 1;" 
    data = mysql.getdata(query)
    mydb.close()
    return jsonify(firstName=data[0], lastName=data[1], imageURL=data[2])
    