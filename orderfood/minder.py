import functools
from .db import MySQL

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
import requests
import json

bp = Blueprint('minder', __name__, url_prefix='/minder')

@bp.route("/modal")
def modal():

    # Logging data to check what is posted to api
    content = request.json
    data = json.dumps(content)
    with open("./logs",'a+') as f:
        f.write(data)

    mysql = MySQL()
    db_meta = mysql.load_db_meta()
    mydb = mysql.create_mysql_db_object(db_meta['host'],db_meta['username'], db_meta['password'], db_meta['port'], db_meta['db'])
    query = "SELECT interest FROM app_users;"
    data = mysql.getData(mydb, query)
    mydb.close()
    if data[0][0] is None: 
        return "Baby please enter your interest"
    return render_template("modal.html")

@bp.route("/yes")
def yes():
    #r = requests.get("https://api.flock.co/v1/chat.sendMessage?to=u:olhoyhclihiyyhhy&text=" + "Awesome Akshay" + "&token=b9c7b452-1145-4797-87cb-c92991fb6732")
    return "200"

@bp.route("/no")
def no():
    #r = requests.get("https://api.flock.co/v1/chat.sendMessage?to=u:olhoyhclihiyyhhy&text=" + "Awesome Harsh" + "&token=b9c7b452-1145-4797-87cb-c92991fb6732")
    return "200"

@bp.route("/randomUser")
def random_image():
    mysql = MySQL()
    db_meta = mysql.load_db_meta()
    mydb = mysql.create_mysql_db_object(db_meta['host'],db_meta['username'], db_meta['password'], db_meta['port'], db_meta['db'])
    query = "SELECT * FROM user_details where gender = 'F' ORDER BY RAND() LIMIT 1;"
    data = mysql.getData(mydb, query)
    mydb.close()
    return jsonify(firstName=data[0][1], lastName=data[0][2], imageURL=data[0][3], userId=data[0][0])
