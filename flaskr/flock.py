import functools

from flask import (
    Blueprint, flash, g, redirect, jsonify, render_template, request, session, url_for
)
import json
import requests
import re
from porter2stemmer import Porter2Stemmer

bp = Blueprint('flock', __name__, url_prefix='/')

@bp.route("/install", methods=['GET', 'POST'])
def install():
    return "yay you have installed food app"

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
    if content["name"] == "client.slashCommand":
        if content["command"] == "orderfood":
            menu_str = ""
            with open("butler_logs") as fbutler:
                menu_str = prepare_menu(json.load(fbutler)["text"])
            r = send_message(menu_str)
            return jsonify(text=menu_str)


    #requests.get("https://api.flock.co/v1/chat.sendMessage?to=someuser&text=Thanks&token=sometoken")
    #r = send_message()
    return "yay"
    #return jsonify(text=str(r))

# This function is used to send a message to a person
#TODO I need to pass an id to send message to a person
def send_message(message):
    r = requests.get("https://api.flock.co/v1/chat.sendMessage?to=someuser&text=" + message + "&token=sometoken")
    return r.status_code

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
