from flask import (
    Blueprint, flash, g, redirect, jsonify, render_template, request, session, url_for
)

bp = Blueprint('flock', __name__, url_prefix='/user')

@bp.route("/interest", methods=['POST'])
def interest():
    userId = request.args.get('userId')
    return "yay you have installed food app"
