# modules
from flask import Flask
import redis.exceptions
from .Config import Config
from flask_redis import FlaskRedis
from flask_cors import CORS
import redis

# Configure redis
redis_client = FlaskRedis()

# blueprints
from app.routes.index import bp_index
from app.routes.accidents.accidents import bp_accidents
from app.routes.paths.paths import bp_paths
from app.routes.cars.cars import bp_cars

def create_app(config=Config):
  app = Flask(__name__)
  app.config.from_object(config)
  redis_client.init_app(app)
  CORS(app, supports_credentials=True)
  
  app.register_blueprint(bp_index, url_prefix='/')
  app.register_blueprint(bp_accidents, url_prefix='/accidents')
  app.register_blueprint(bp_paths, url_prefix='/paths')
  app.register_blueprint(bp_cars, url_prefix='/cars')
  
  return app