# modules
from flask import Flask
import redis.exceptions
from .Config import Config
from flask_redis import FlaskRedis
import redis

# Configure redis
redis_client = FlaskRedis()

# blueprints
from app.routes.routes import bp_routes
from app.routes.accidents.accidents import bp_accidents

def create_app(config=Config):
  app = Flask(__name__)
  app.config.from_object(config)
  redis_client.init_app(app)
  
  app.register_blueprint(bp_routes, url_prefix='/test')
  app.register_blueprint(bp_accidents, url_prefix='/accidents')

  @app.route('/')
  def index():
    return 'Hello, World!'
  
  return app