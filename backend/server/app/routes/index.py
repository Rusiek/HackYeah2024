from flask import Blueprint, jsonify
import redis

bp_index = Blueprint('index', __name__)

# test route - delete later
@bp_index.route('/')
def index():
  return jsonify({'status': 'success', 'messege': 'Connected to server!', 'code': '200'})
