from flask import (
    Blueprint, flash, g, redirect, jsonify, render_template, request, session, url_for
)

bp = Blueprint('user', __name__, url_prefix='/user')

@bp.route("/interest", methods=['POST'])
def interest():
    userId = request.args.get('userId')
    interest = request.args.get('interest')
    return "yay you have installed food app"
