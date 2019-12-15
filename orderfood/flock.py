import functools

from flask import (
    Blueprint, flash, g, redirect, jsonify, render_template, request, session, url_for
)
import json
import requests
import re
from porter2stemmer import Porter2Stemmer
from .db import MySQL

bp = Blueprint('flock', __name__, url_prefix='/')

@bp.route("/install", methods=['GET', 'POST'])
def install():
    return render_template("welcome.html")

@bp.route("/flockhook", methods=['GET', 'POST'])
def butler_messages():
    content = request.json
    with open("butler_logs",'w') as f2:
        f2.write(json.dumps(content))
    return "200"

@bp.route("/slashcommand", methods=['GET', 'POST'])
def food():
    if request.method == 'GET':
        return "from get"
    if request.method == 'POST':
        return "from post"
    #content = request.args['flockEvent']
    #data = json.dumps(content)
    #with open("./slashlogs", "a+") as f1:
        #f1.write(content)
    #return "<h1> Hello </h1>"

@bp.route("/events", methods=['GET', 'POST'])
def events():
    content = request.json
    data = json.dumps(content)
    with open("./logs",'a+') as f:
        f.write(data)

    #TODO For all these database opertions ideally we should create Model package, Curiosity to finish this app quickly forcing me to do it... feeling excited and bad at the same time
    if content["name"] == "app.install":
        insert_query = "INSERT INTO app_users (user_id, token, is_valid) VALUES ('" +  str(content['userId']) + "', '" + str(content['userToken']) + "',1);"
        mysql = MySQL()
        db_meta = mysql.load_db_meta()
        mydb = mysql.create_mysql_db_object(db_meta['host'],db_meta['username'], db_meta['password'], db_meta['port'], db_meta['db'])
        mysql.cudOperations(mydb, insert_query)
        mydb.close()
        return "user successfully installed this app"

    if content["name"] == "app.uninstall":
        del_query = "DELETE FROM app_users where user_id = '" + str(content['userId']) + "';"
        mysql = MySQL()
        db_meta = mysql.load_db_meta()
        mydb = mysql.create_mysql_db_object(db_meta['host'],db_meta['username'], db_meta['password'], db_meta['port'], db_meta['db'])
        mysql.cudOperations(mydb, del_query)
        mydb.close()
        return "user uninstalled app, all his data got deleted"



    #Todo This is code for orderfood app to get menu, it will be used in some other app
    # if content["name"] == "client.slashCommand":
    #     if content["command"] == "orderfood":
            # menu_str = ""
            # with open("butler_logs") as fbutler:
            #     menu_str = prepare_menu(json.load(fbutler)["text"])
            # r = send_message(menu_str)
            # return jsonify(text=menu_str)

    return "yay"
    #return jsonify(text=str(r))

# This will prepare menu in string format for us
def prepare_menu(posted_menu):
    menu_str = ""
    menu = stringtoterms(posted_menu)
    for i in range(0, len(menu)):
        if "   " not in menu[i] and not hasNumbers(menu[i]) and not any(badword in menu[i].lower() for badword in ["menu", "veg","good", "any", "one"]) and len(menu[i]) >2:
            menu_str += menu[i] + "\n"
    return menu_str

# Function to check, whether a string contain a number
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

# Function to get all terms from one doc, delimiters modified a little bit to just get menu
def stringtoterms(string, stemming=False):
    delimiters = ".","(c)","?","-","#","*","_","/","(",")","!","'",'"',";",":","&","<",">","\r","\n","\t"
    regexPattern = '|'.join(map(re.escape, delimiters))
    refinedlist = re.split(regexPattern, string)
    termlist = []

    for word in refinedlist:
        if stemming == True:
            word = stemmer.stem(word)
        termlist.append(word)

    termlist = filter(None,termlist)
    #print termlist
    return list(termlist)
