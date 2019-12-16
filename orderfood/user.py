from flask import (
    Blueprint, flash, g, redirect, jsonify, render_template, request, session, url_for
)

from .db import MySQL

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route("/interest", methods=['GET','POST'])
def interest():
    if request.method == 'POST':
        userId = request.form.get('userId')
        interest = request.form.get('interest')
        with open("./logs",'a+') as f:
            f.write(str(interest))
            f.write(str(userId))
        update_query = "UPDATE app_users SET interest = '" + str(interest) + "' where user_id = '" + str(userId) + "';"
        mysql = MySQL()
        db_meta = mysql.load_db_meta()
        mydb = mysql.create_mysql_db_object(db_meta['host'],db_meta['username'], db_meta['password'], db_meta['port'], db_meta['db'])
        mysql.cudOperations(mydb, update_query)
        mydb.close()

    return "200"
