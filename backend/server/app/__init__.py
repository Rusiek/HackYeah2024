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

def create_app(config=Config):
  app = Flask(__name__)
  app.config.from_object(config)
  redis_client.init_app(app)
  
  app.register_blueprint(bp_routes)

  
  return app