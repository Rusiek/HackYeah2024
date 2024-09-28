from flask import Blueprint, current_app
from app import redis_client
import redis

bp_routes = Blueprint('routes', __name__)

# test route - delete later
@bp_routes.route('/')
def index():
  redis_client.set('mykey', 'Hello, Redis!')
  value = redis_client.get('mykey')
  return f'The value of mykey is: {value.decode("utf-8")}'

@bp_routes.route('/ping')
def ping_redis():
    try:
        redis_client.ping()
        return 'Connected to Redis!'
    except redis.exceptions.ConnectionError:
        return 'Failed to connect to Redis.'

