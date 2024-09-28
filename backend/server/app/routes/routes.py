from flask import Blueprint
from app import redis_client
import redis

bp_routes = Blueprint('routes', __name__)

# test route - delete later
@bp_routes.route('/')
def index():
  try:
    redis_client.ping()
    return 'Connected to Redis!'
  except redis.exceptions.ConnectionError:
      return 'Failed to connect to Redis.'
