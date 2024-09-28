from flask import Blueprint, jsonify
from app import redis_client
import redis

bp_index = Blueprint('index', __name__)

# test route - delete later
@bp_index.route('/')
def index():
  try:
    redis_client.ping()
    return jsonify({'status': 'success', 'messege': 'Connected to redis!', 'code': '200'})
  except redis.exceptions.ConnectionError:
      return jsonify({'error':{'type': 'Internal Server Error', 'messege': 'Could not connect to redis'}, 'code': '500'}), 500
